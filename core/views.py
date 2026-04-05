from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.db.models import Sum
from .models import FinancialRecord
from .forms import RecordForm



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Username and password are required')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'All fields are required')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')

        if len(password) < 4:
            messages.error(request, 'Password must be at least 4 characters')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def total_income(user):
    if not user.is_authenticated:
        return 0
    return FinancialRecord.objects.filter(user=user, type='income').aggregate(Sum('amount'))['amount__sum'] or 0


def total_expense(user):
    if not user.is_authenticated:
        return 0
    return FinancialRecord.objects.filter(user=user, type='expense').aggregate(Sum('amount'))['amount__sum'] or 0


def balance(user):
    if not user.is_authenticated:
        return 0
    return total_income(user) - total_expense(user)

def category_breakdown(user):
    if not user.is_authenticated:
        return []
    return FinancialRecord.objects.filter(user=user).values('category').annotate(total=Sum('amount'))


def monthly_totals(user):
    if not user.is_authenticated:
        return []
    return FinancialRecord.objects.filter(user=user).extra({'month': "strftime('%%m', date)"}).values('month').annotate(total=Sum('amount'))


def recent_activity(user):
    if not user.is_authenticated:
        return []
    return FinancialRecord.objects.filter(user=user).order_by('-created_at')[:5]

@login_required
def dashboard(request):
    context = {
        'income': total_income(request.user),
        'expense': total_expense(request.user),
        'balance': balance(request.user),
        'categories': category_breakdown(request.user),
        'monthly': monthly_totals(request.user),
        'recent': recent_activity(request.user)
    }
    return render(request, 'dashboard.html', context)


@login_required
def create_record(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.user = request.user
        record.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})


@login_required
def list_records(request):
    records = FinancialRecord.objects.filter(user=request.user)

    # Filters
    type_filter = request.GET.get('type')
    category = request.GET.get('category')
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')

    if type_filter:
        records = records.filter(type=type_filter)
    if category:
        records = records.filter(category=category)
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])

    return render(request, 'list.html', {'records': records})

@login_required
def update_record(request, id):
    record = get_object_or_404(FinancialRecord, id=id, user=request.user)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'form.html', {'form': form})


"""@login_required
def delete_record(request, id):
    record = get_object_or_404(FinancialRecord, id=id, user=request.user)
    record.delete()
    return redirect('dashboard')"""
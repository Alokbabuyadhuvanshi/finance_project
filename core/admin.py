from django.contrib import admin
from .models import FinancialRecord, User
from .views import balance
class FinancialRecordInline(admin.TabularInline):
    model = FinancialRecord
    extra = 0
    fields = ('amount', 'type', 'category', 'date')

class UserAdmin(admin.ModelAdmin):
    inlines = [FinancialRecordInline]
    list_display = ('username', balance)
    search_fields = ('username',)

class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'category', 'date')
    list_filter = ('type', 'category', 'date')
    search_fields = ('category', 'notes')
    ordering = ('-date',)


admin.site.register(User, UserAdmin)
admin.site.register(FinancialRecord, FinancialRecordAdmin)


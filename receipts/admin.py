from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

@admin.register(ExpenseCategory)
class ExpenseCatergoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "id",
    )

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "total",
        "tax",
        "date",
        "purchaser",
        "category",
        "account",
    )

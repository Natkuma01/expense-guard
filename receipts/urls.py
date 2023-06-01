from django.urls import path
from receipts.views import show_receipt, create_receipt, account_list, category_list, create_expense_category

urlpatterns = [
    path("categories/create/", create_expense_category, name="create_category"),
    path("accounts/", account_list, name="account_list"),
    path("categories/", category_list, name="category_list"),
    path("create/", create_receipt, name="create_receipt"),
    path("", show_receipt, name="home"),
]
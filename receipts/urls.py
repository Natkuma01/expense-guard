from django.urls import path
from receipts.views import show_receipt, create_receipt, account_list, category_list

urlpatterns = [
    path("accounts/", account_list, name="account_list"),
    path("categories/", category_list, name="category_list"),
    path("create/", create_receipt, name="create_receipt"),
    path("", show_receipt, name="home"),
]
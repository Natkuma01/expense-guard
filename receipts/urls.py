from django.urls import path
from receipts.views import show_receipt, create_receipt

urlpatterns = [
    path("create/", create_receipt, name="create_receipt"),
    path("", show_receipt, name="home"),
]
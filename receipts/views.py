from django.shortcuts import render
from receipts.models import Receipt

def show_receipt(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/main.html", context)

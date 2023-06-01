from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

@login_required
def show_receipt(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/main.html", context)

from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm

@login_required
def show_receipt(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/main.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            form.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form
    }
    return render(request, "receipts/create.html", context)

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/categories.html", context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts
    }
    return render(request, "receipts/accounts.html", context)

@login_required
def create_expense_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense_category = form.save(False)
            expense_category.owner = request.user
            form.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()

    context = {
        "form": form
    }
    return render(request, "receipts/categories/create.html", context)

@login_required
def create_account(request):
    if request.method =="POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            form.save()
            return redirect("account_list")
    else:
        form = AccountForm()

    context = {
        "form": form
    }
    return render(request, "receipts/accounts/create.html", context)
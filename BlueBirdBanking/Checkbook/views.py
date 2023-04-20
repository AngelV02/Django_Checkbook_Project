from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.

# This function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # Retrieves Transaction form

    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if form is submitted retrieve which account the user wants to view
        return balance(request, pk)

    content = {'form': form}

    return render(request, 'checkbook/index.html', content)


# This function will render the create new account page
def create_account(request):
    return render(request, 'checkbook/CreateNewAccount.html')


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # Retrieves the requested account using its primary key
    transactions = Transaction.Transaction.filter(account=pk)  # Retries all of that account's transaction
    current_total = account.initial_deposit  # Create account variable, starting with initial deposit value
    table_contents = {}  # Creates a dictionary into which transaction information will be placed

    for t in transactions: # loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount # if deposit add amount to balance
            table_contents.update({t: current_total}) # Add transaction and total to the dictionary

        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}

    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the create new account page
def transaction(request):
    return render(request, 'checkbook/AddTransaction.html')


# this function wiill render the create new Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve the account form

    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    content = {'form': form}

    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieve the account form

    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)

    content = {'form': form}

    return render(request, 'checkbook/AddTransaction.html', content)

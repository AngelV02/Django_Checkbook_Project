from django.db import models


# Create your models here.

class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # defines the model manager for accounts
    Accounts = models.Manager()

    # allows references to a specific account be returned as the owners name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


Transactiontypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# Creates the transaction Model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=Transactiontypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Defines the model Manager for Transactions
    Transaction = models.Manager()
from django.db import models

# Create your models here.

class Borrower(models.Model):
    name = models.CharField(max_length=200)
    loan_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100)
    loan_amount = models.IntegerField()
    amount_paid = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.state})'
    
class Stateloan(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)
    amount_lended = models.IntegerField()
    amount_recovered = models.IntegerField()

    def __str__(self):
        return self.state_name
    

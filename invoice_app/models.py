# invoice_app/models.py
from django.db import models


class Invoice(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.invoice_number

class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.description}"

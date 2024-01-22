# invoice_app/tests.py
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Invoice, InvoiceDetails


class InvoiceAPITestCase(APITestCase):

    def test_create_invoice(self):
        data = {
            'date': '2024-01-22',
            'invoice_number': 'INV-001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Product A',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'price': '20.00',
                }
            ]
        }
        response = self.client.post(reverse('invoice-list-create'), data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_invoice_details(self):
        invoice = Invoice.objects.create(date='2024-01-22', invoice_number='INV-002', customer_name='Jane Doe')
        InvoiceDetails.objects.create(invoice=invoice, description='Product B', quantity=3, unit_price='15.00', price='45.00')

        response = self.client.get(reverse('invoice-details', args=[invoice.pk]))
        self.assertEqual(response.status_code, 200)

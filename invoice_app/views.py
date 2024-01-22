# invoice_app/views.py
from rest_framework import generics
from .models import Invoice, InvoiceDetails
from .serializers import InvoiceSerializer, InvoiceDetailsSerializer


class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

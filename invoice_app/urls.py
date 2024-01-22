# invoice_app/urls.py
from django.urls import path
from .views import InvoiceListCreateView, InvoiceDetailsView


urlpatterns = [
    path('invoice/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/', InvoiceDetailsView.as_view(), name='invoice-details'),
]

from rest_framework import viewsets
from api.models import Customer
from api.serializer import CustomerSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    """Displaying the customer's data"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

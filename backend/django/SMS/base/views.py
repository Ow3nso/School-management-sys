# ----- 3rd Party Libraries -----
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# ----- In-Built Libraries -----
from base.models import Contact
from base.serializers import ContactSerializer

# ----- CPU views -----

class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


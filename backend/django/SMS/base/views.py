# ----- 3rd Party Libraries -----
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# ----- In-Built Libraries -----
from base.models import Contact
from base.serializers import ContactSerializer

# ----- CPU views -----

class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)

    def create(self, request, *args, **kwargs):
        try:
            # Your custom logic for creating an object
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            # Handle the exception and return an appropriate response
            #print(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            


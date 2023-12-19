# ----- 3rd Party Libraries -----
from rest_framework import serializers

# ----- In-Built Library -----
from base.models import Contact

# ----- model serializers -----
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
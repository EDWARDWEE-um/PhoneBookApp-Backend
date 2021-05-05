
from rest_framework import serializers
from .models import Contacts

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = (
            'name',
            'phone_number',
        )
    
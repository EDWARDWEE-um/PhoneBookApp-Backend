from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contacts
from django.shortcuts import get_object_or_404
# Create your views here.


class ContactList(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Contacts, slug=item)

    def get_queryset(self):
        return Contacts.objects.all()
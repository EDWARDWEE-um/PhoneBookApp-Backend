from .views import ContactList, Contacts
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'phone'

router = DefaultRouter()
router.register('', ContactList, basename='contact')


urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ['owner', 'name', 'contact', 'email', 'spam']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(view_name='contact-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'contacts']
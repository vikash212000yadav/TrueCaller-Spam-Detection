from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Contact
from .permissions import IsOwner
from .serializers import ContactSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, filters
from rest_framework.reverse import reverse


# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'contact', 'email', 'spam']
    permission_classes = [permissions.IsAuthenticated,
                          IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'contacts': reverse('contact-list', request=request, format=format)
    })

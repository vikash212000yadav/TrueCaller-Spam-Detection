from django.urls import path, include
from rest_framework.routers import DefaultRouter
from truecallerapi import views
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

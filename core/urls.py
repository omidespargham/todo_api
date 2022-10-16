from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views

app_name = 'core'

urlpatterns = [
     path('token-auth/', token_views.obtain_auth_token)
    
]



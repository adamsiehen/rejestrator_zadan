from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import RegisterView

urlpatterns = [
    path('api/', include('myapp.api_urls')),
    path('api/login/', obtain_auth_token),
    path('api/register/', RegisterView.as_view()),
]


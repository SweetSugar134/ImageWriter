from django.urls import path
from .views import index, RegistrationUserView


urlpatterns = [
    path('', index, name='home'),
    path('reg', RegistrationUserView.as_view(), name='registration'),
]

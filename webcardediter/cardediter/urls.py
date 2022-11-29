from django.urls import path
from .views import index, RegistrationUserView, LoginUser, LogoutUser


urlpatterns = [
    path('', index, name='home'),
    path('reg/', RegistrationUserView.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='registration'),
    path('logout/', LogoutUser.as_view(), name='registration'),
]

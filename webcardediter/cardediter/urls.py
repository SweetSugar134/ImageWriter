from django.urls import path
from .views import index, RegistrationUserView, LoginUser, LogoutUser, change_template, upload_own_image


urlpatterns = [
    path('', index, name='home'),
    path('reg/', RegistrationUserView.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('ch_temp/', change_template, name='temp_change'),
    path('own_image/', upload_own_image, name='upload_image'),
]

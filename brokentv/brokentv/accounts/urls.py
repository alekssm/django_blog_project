from django.urls import path

from brokentv.accounts.views import UserLoginView, UserRegisterView, UserLogoutView, ProfileDetailsView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
    path('register/', UserRegisterView.as_view(), name="register user"),
    path('profile/int:<pk>/', ProfileDetailsView.as_view(), name='profile details'),
)
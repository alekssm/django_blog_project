from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from brokentv.accounts.forms import UserRegistrationForm


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('show index')


class UserLogoutView(LogoutView):

    def get_success_url(self):
        return reverse_lazy('show index')


class UserProfileView:
    pass



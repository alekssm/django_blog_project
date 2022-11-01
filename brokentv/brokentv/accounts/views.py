from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from brokentv.accounts.forms import UserRegistrationForm

UserModel = get_user_model()


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


# class UserDeleteView(DeleteView):
#     # specify the model you want to use
#     # form_class = DeleteUserForm
#     model = UserModel
#     success_url = reverse_lazy('show index')
#
#     template_name = "accounts/delete_user_page.html"


# class UserEditView(UpdateView):
#     template_name = 'accounts/update_user_page.html'
#     form_class = EditUserProfileForm


class UserProfileView:
    pass



from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from brokentv.accounts.forms import UserRegistrationForm
from brokentv.accounts.models import Profile
from brokentv.web.models import Post

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


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = list(Post.objects.filter(author=self.object.user))

        total_posts = len(posts)

        context.update({
            'posts': posts,
            'total_posts': total_posts,
        })
        return context




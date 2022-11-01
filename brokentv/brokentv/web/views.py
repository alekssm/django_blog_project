from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from brokentv.web.models import Profile, Post


class ShowIndex(TemplateView):
    template_name = 'web/index.html'


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'web/profile_details.html'
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

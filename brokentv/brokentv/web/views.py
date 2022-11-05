from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from brokentv.web.models import Post


class ShowIndex(TemplateView):
    template_name = 'web/index.html'

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import WeakAura


class IndexView(generic.ListView):
    template_name = 'wadb/index.html'
    context_object_name = 'weakaura_list'

    def get_queryset(self):
        return WeakAura.objects.order_by('-datetime_created')[:5]


class DetailView(generic.DetailView):
    model = WeakAura
    template_name = 'wadb/detail.html'

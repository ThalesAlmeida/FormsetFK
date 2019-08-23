from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from django.views.generic.list import ListView
from .models import Service
from .forms import ServiceForm
from django.urls import reverse_lazy


class ServiceCreateView(CreateView):
    model = Service
    template_name = "enterprise/service_new.html"
    form_class = ServiceForm
    success_message = "Endereço e Contatos alterados com sucesso!"

    def get_success_url(self):
        return reverse_lazy('author:enterprise-list')


class ServiceListView(ListView):
    model = Service
    template_name = "enterprise/service_list.html"

# Create your views here.

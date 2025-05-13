from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Automovil

class AutomovilListView(LoginRequiredMixin, ListView):
    model = Automovil
    template_name ='automoviles_list.html'
    context_object_name = 'automoviles'

class AutomovilDetailView(LoginRequiredMixin, DetailView):
    model = Automovil
    template_name = 'automovil_detail.html'
    context_object_name = 'automovil'

class AutomovilCreateView(CreateView):
    model = Automovil
    fields = ['marca', 'modelo', 'anio', 'color', 'precio']  # ajusta a tus campos
    template_name = 'automovil_form.html'
    success_url = reverse_lazy('automoviles:listar')

class AutomovilUpdateView(UpdateView):
    model = Automovil
    fields = ['marca', 'modelo', 'anio', 'color', 'precio']
    template_name = 'automovil_form.html'
    success_url = reverse_lazy('automoviles:listar')

class AutomovilDeleteView(DeleteView):
    model = Automovil
    template_name = 'automovil_confirm_delete.html'
    success_url = reverse_lazy('automoviles:listar')

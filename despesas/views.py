from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages


from . models import Despesa,CategoriaDespesa
from . form import DespesaForm
# Create your views here.


class DespesaCreate(LoginRequiredMixin,CreateView):
    model = Despesa
    #form_class = DespesaForm
    fields=['name','value','typeDespesa','date','categoria']
    template_name = 'despesas/despesa_form.html'
    success_url = reverse_lazy("despesas:list_Despesas")
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(DespesaCreate,self).form_valid(form)

class DespesasListView(LoginRequiredMixin, ListView):
    model = Despesa
    context_object_name = 'list_Despesas'
    def get_queryset(self):
        user = self.request.user
        return Despesa.objects.filter(user = user)
    paginate_by = 4


        
class DespesasUpdateView(LoginRequiredMixin, UpdateView):
    model = Despesa
    #form_class  = DespesaForm
    fields=['name','value','typeDespesa','date','categoria']
    success_url = reverse_lazy("despesas:list_Despesas")

class DespesasDeleteView(LoginRequiredMixin, DeleteView):
    model = Despesa
    context_object_name = 'despesas'
    success_url = reverse_lazy('despesas:list_Despesas')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(DespesasDeleteView,self).form_valid(form)

class CategoriaDespesaCreate(LoginRequiredMixin,CreateView):
    model = CategoriaDespesa
    fields = ['name']
    template_name = 'categoriadespesas/categoriadespesas_form.html'
    success_url = reverse_lazy("despesas:list_Despesas")
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CategoriaDespesaCreate,self).form_valid(form)
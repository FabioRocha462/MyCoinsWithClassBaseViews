from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages

#my form and models
from . models import Receita,CategoriaReceita
from . form import ReceitaForm
# Create your views here.

class ReceitaCreateView(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = ReceitaForm
    #fields = ['name','value','typeReceita', 'date', 'categoria']
    template_name = 'receitas/receita_form.html'
    success_url = reverse_lazy("receitas:list_Receitas")
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(ReceitaCreateView,self).form_valid(form)

class ReceitaListView(LoginRequiredMixin, ListView):
    model = Receita
    context_object_name = 'list_Receitas'
    def get_queryset(self):
        user = self.request.user
        return Receita.objects.filter(user = user)
    paginate_by = 4

class CategoriaReceitaCreateView(LoginRequiredMixin, CreateView):
    model = CategoriaReceita
    fields = ['name']
    template_name = 'categoriareceita/categoriareceita_form.html'
    success_url = reverse_lazy("receitas:list_Receitas")
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CategoriaReceitaCreateView,self).form_valid(form)

class ReceitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Receita
    form_class  = ReceitaForm
    success_url = reverse_lazy("receitas:list_Receitas")

class ReceitaDeleteView(LoginRequiredMixin, DeleteView):
    model = Receita
    context_object_name = 'receitas'
    success_url = reverse_lazy('receitas:list_Receitas')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(ReceitaDeleteView,self).form_valid(form)    

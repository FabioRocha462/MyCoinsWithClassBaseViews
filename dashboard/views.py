from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from despesas.models import Despesa
from receitas.models import Receita
# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard/dashboard.html"



def despesanuais(request):
    if request.method == 'GET':
        meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        user = request.user
        print(user.id)
        despesas = Despesa.objects.filter(user=user)
        if  len(despesas) > 0:
            valoresPorMEs = []
            for i in meses:
                sum = 0
                for despesa in despesas:
                    if despesa.date.month == i:
                        sum += despesa.value
                valoresPorMEs.append(sum)
            return JsonResponse({'valores': valoresPorMEs, 'meses': meses,"user": user.id})
        else:
            return JsonResponse({'msg': "não tem despesas deste ano"})

def valores(request):
    if request.method == 'GET':
        user = request.user
        despesas = Despesa.objects.filter(user=user)
        receitas = Receita.objects.filter(user=user)
        somaDespesa = 0
        somaReceita = 0
        if len(despesas) > 0:
            for despesa in despesas:
                somaDespesa += despesa.value
        if len(receitas) > 0:
            for receita in receitas:
                somaReceita += receita.value
        return JsonResponse({'saldo':somaReceita - somaDespesa})




        
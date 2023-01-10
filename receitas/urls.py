from django.urls import path

from . views import ReceitaCreateView,ReceitaListView,CategoriaReceitaCreateView, ReceitaUpdateView, ReceitaDeleteView
app_name = "receitas"

urlpatterns = [
    path('create', ReceitaCreateView.as_view(), name='create_Receitas'),
    path('list',ReceitaListView.as_view(), name='list_Receitas'),
    path('categoria_receita_create', CategoriaReceitaCreateView.as_view(), name='categoria_receita_create'),
    path('update/<int:pk>', ReceitaUpdateView.as_view(), name='update_Receitas'),
    path('delete/<int:pk>', ReceitaDeleteView.as_view(), name='delete_Receitas'),

]
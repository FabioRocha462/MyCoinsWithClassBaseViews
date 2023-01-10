from django.urls import path
from . views import DespesaCreate, DespesasListView,CategoriaDespesaCreate,DespesasUpdateView,DespesasDeleteView

app_name = "despesas"
urlpatterns = [
    path("create",DespesaCreate.as_view(),name="create_Despesa"),
    path("list/",DespesasListView.as_view(),name="list_Despesas"),
    path("categoria_despesas_create",CategoriaDespesaCreate.as_view(),name="categoria_desespesa_create"),
    path("update/<int:pk>", DespesasUpdateView.as_view(),name="update_Despesas"),
    path("delete/<int:pk>", DespesasDeleteView.as_view(),name="delete_Despesas"),
]
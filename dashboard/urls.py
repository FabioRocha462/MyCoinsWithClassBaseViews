from django.urls import path
from . views import DashboardView,despesanuais,valores
app_name = "despesas"
urlpatterns = [
    path("dashboardview/", DashboardView.as_view(), name="dashboard"),
    path('despesasanuais/',despesanuais, name="despesasanuais"),
    path('valores/',valores, name="valores"),
]

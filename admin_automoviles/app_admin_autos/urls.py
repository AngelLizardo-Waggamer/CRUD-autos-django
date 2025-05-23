from django.urls import path
from . import views

app_name = 'automoviles'

urlpatterns = [
    path('', views.AutomovilListView.as_view(), name='listar'),
    path('crear/', views.AutomovilCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.AutomovilDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.AutomovilUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.AutomovilDeleteView.as_view(), name='eliminar'),
]
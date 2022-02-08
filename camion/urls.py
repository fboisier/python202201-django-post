from django.urls import path
from . import views

# camion/

app_name = 'camion'

urlpatterns = [
    path('', views.index, name='index' ),
    path('success', views.resultados, name='success' ),
]

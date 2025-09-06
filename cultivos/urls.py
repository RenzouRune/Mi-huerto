from django.urls import path
from .views import listar_cultivos, detalle_cultivo, recomendar_cultivos

urlpatterns = [
    path('', listar_cultivos, name='listar_cultivos'),
    path('detalle/<str:nombre>/', detalle_cultivo, name='detalle_cultivo'),
    path('recomendacion/', recomendar_cultivos, name='recomendar_cultivos'),

]

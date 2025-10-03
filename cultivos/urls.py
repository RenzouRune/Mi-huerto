from django.urls import path
from .views import listar_cultivos, detalle_cultivo, recomendar_cultivos, registrar_cultivo

urlpatterns = [
    path('', listar_cultivos, name='listar_cultivos'),
    path('agregar/', registrar_cultivo, name='registrar_cultivo'),
    path('detalle/<str:nombre>/', detalle_cultivo, name='detalle_cultivo'),
    path('recomendacion/', recomendar_cultivos, name='recomendar_cultivos'),

]

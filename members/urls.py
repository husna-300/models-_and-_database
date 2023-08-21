from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('alifmobi/', views.alifmobi, name='alifmobi'),
    path('visa/', views.visa, name='visa'),
    path('salom/', views.salom, name='salom'),
    path('carfinancing/', views.carfinancing, name='carfinancing'),
    path('alifshop/', views.alifshop, name='alifshop'),
    path('deposits/', views.deposits, name='deposits'),
    path('transfers/', views.transfers, name='transfers'),
    path('alifonline/', views.alifonline, name='alifonline'),
   
]
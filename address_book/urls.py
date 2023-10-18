from django.urls import path
from django.urls import include
from . import views

app_name = 'address_book'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail'),
]

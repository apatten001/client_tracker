from django.urls import path
from .views import client_list_view, ClientProfileView

app_name = 'client'
urlpatterns = [
    path('list/', client_list_view, name='list'),
    path('<int:pk>/', ClientProfileView.as_view(), name='profile'),

]
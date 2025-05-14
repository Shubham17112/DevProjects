from django.urls import path
from . import views
app_name = 'to_do'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:id>', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
]

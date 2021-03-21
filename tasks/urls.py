from django.urls import path
from . import views
urlpatterns = [
   path('', views.addtasks, name = 'tasks'),
   path('editTask/<int:id>/', views.editTask,name='editTask'),
   path('delete/<str:id>', views.delete, name='delete')
]

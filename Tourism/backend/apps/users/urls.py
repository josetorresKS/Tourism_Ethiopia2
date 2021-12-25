from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.UserList.as_view(), name='user_list'),
# ]

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('add/', views.UserAdd.as_view(), name='user_add'),
    path('delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
]

# user_app/urls.py
from django.urls import path
from .views import UserListView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),    
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]

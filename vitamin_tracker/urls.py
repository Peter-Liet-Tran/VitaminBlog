from django.urls import path
from . import views
from .views import (
       UserVitaminListView, VitaminCreateView, VitaminUpdateView, VitaminDeleteView)

urlpatterns = [
    path('user/<str:username>', UserVitaminListView.as_view(), name='user-posts'),
    path('vitamin/new/', VitaminCreateView.as_view(), name='post-create'),
    path('vitamin/<int:pk>/update', VitaminUpdateView.as_view(), name='post-update'),
    path('vitamin/<int:pk>/delete', VitaminDeleteView.as_view(), name='post-delete'), 
]

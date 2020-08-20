from django.urls import path 
from . import views
from .views import (
       VitaminDetailView, UserVitaminListView, VitaminCreateView, VitaminUpdateView, VitaminDeleteView)

urlpatterns = [
    path('user/', UserVitaminListView.as_view(),
        name='user-vitamins'),
    path('vitamin/new/', VitaminCreateView.as_view(), name='vitamin-create'),
    path('vitamin/<int:pk>/update', VitaminUpdateView.as_view(), name='vitamin-update'),
    path('vitamin/<int:pk>/delete', VitaminDeleteView.as_view(), name='vitamin-delete'), 
    path('vitamin/<int:pk>/', VitaminDetailView.as_view(), name='vitamin-detail'),
]

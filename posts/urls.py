"""Posts URLs Configuration."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostListView.as_view(),
        name='feed'
    ),

    path(
        route='new/',
        view=views.PostCreateView.as_view(),
        name='create'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]

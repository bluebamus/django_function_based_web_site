from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.board_list, name="board_list"),
    path("write/", views.board_write, name="board_write"),
    path("detail/<int:pk>/", views.board_detail, name="board_detail"),
    path("delete/<int:pk>/", views.board_delete, name="board_delete"),
    path("update/<int:pk>/", views.board_update, name="board_update"),
    path("like/<int:pk>/", views.likes, name="board_like"),
]

from django.urls import path
from . import views

urlpatterns = [    
    path("register/", views.register, name="register"),    
    path("login/<int:select_nunber>", views.login_new_table, name="login-new-table"),
    path("logout/", views.logout, name="logout"),
]

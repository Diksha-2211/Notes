# notes/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

     # Notes
    path('create/', views.create_note, name='create_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]

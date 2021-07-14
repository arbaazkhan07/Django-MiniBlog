from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-post/', views.addPost, name='addPost'),
    path('edit-post/<int:id>', views.editPost, name='editPost'),
    path('delete-post/<int:id>', views.deletePost, name='deletePost'),
    path('logout/', views.userLogout, name='logout'),
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
]

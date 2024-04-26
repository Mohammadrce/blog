from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.register_user, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('edit/', views.user_edit, name="edit")
]

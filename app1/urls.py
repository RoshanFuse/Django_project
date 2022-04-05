from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.Signup,name='Signup'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user')
]
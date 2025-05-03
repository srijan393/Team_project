from django.urls import path
from . import views

urlpatterns = [
    path('', views.air_quality_list, name='air_quality_list'),
    path('view_data/', views.view_data, name='view_data'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('clear/', views.clear_air_quality_data, name='clear_air_quality_data'),

]

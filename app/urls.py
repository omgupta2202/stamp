# data_collector/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view_open/', views.login_view_open, name='login_view_open'),
    path('save-search-data/', views.save_search_data, name='save_search_data'),
    # path('take_captcha/', views.take_captcha, name='take_captcha'),
    path('save_captcha/', views.save_captcha, name='save_captcha'),
    path('save_captcha2/', views.save_captcha2, name='save_captcha2'),
    
    path('get_tehsils/<int:district_id>/', views.get_tehsils, name='get_tehsils'),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('/save_district/${username}/${selectedDistrictId}/', views.save_district, name='save_district'),
    path('/save_tehsil/${username}/${selectedTehsilId}/', views.save_tehsil, name='save_tehsil'),
    
    

]

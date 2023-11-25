# data_collector/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('open_login_page/', views.open_login_page, name='open_login_page'),
    path('save-search-data/', views.save_search_data, name='save_search_data'),
    # path('take_captcha/', views.take_captcha, name='take_captcha'),
    path('save_captcha/', views.save_captcha, name='save_captcha'),
    path('save_captcha2/', views.save_captcha2, name='save_captcha2'),
    
    path('notification/<str:username>/', views.notification, name='notification'),
    
    path('changedDropdown/<str:username>/<str:changedDropdown>/', views.changedDropdownfun, name='changedDropdown'),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('save_district/<str:username>/<int:selectedDistrictId>/', views.save_district, name='save_district'),
    path('get_tehsils/<int:district_id>/', views.get_tehsils, name='get_tehsils'),
    path('save_tehsil/<str:username>/<int:selectedTehsilId>/', views.save_tehsil, name='save_tehsil'),
    path('get_type_of_areas/<int:tehsil_id>/', views.get_type_of_areas, name='get_type_of_areas'),
    path('save_type_of_area/<str:username>/<str:selectedType_of_area_name>/', views.save_type_of_area, name='save_type_of_area'),
    path('get_sub_area_types/<int:type_of_area_id>/<str:type_of_area_name>/', views.get_sub_area_types, name='get_sub_area_types'),
    path('save_sub_area_type/<str:username>/<int:selectedSub_area_typeId>/', views.save_sub_area_type, name='save_sub_area_type'),
    path('get_ward_number_patwari_numbers/<int:sub_area_type_id>/', views.get_ward_number_patwari_numbers, name='get_ward_number_patwari_numbers'),
    path('save_ward_number_patwari_number/<str:username>/<int:selectedWard_number_patwari_numberId>/', views.save_ward_number_patwari_number, name='save_ward_number_patwari_number'),
    path('get_mohalla_colony_name_society_roads/<int:ward_number_patwari_number_id>/', views.get_mohalla_colony_name_society_roads, name='get_mohalla_colony_name_society_roads'),
    path('save_mohalla_colony_name_society_road/<str:username>/<int:selectedMohalla_colony_name_society_roadId>/', views.save_mohalla_colony_name_society_road, name='save_mohalla_colony_name_society_road'),
]

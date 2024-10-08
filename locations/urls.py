from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('main_locations', views.main_locations, name='main_locations'),
    path('add_state', views.StateCreateView.as_view(), name='add_state'),
    path('state_list', views.StateListView.as_view(), name='state_list'),
    path('update_state/<int:pk>', views.StateUpdateView.as_view(), name='update_state'),
    path('delete_state/<int:pk>', views.StateDeleteView.as_view(), name='delete_state'),
    # locality urls
    path('add_locality', views.LocalityCreateView.as_view(), name='add_locality'),
    path('locality_list', views.LocalityListView.as_view(), name='locality_list'),
    path('update_locality/<int:pk>', views.LocalityUpdateView.as_view(), name='update_locality'),
    path('delete_locality/<int:pk>', views.LocalityDeleteView.as_view(), name='delete_locality'),
    # unity urls
    path('add_unity', views.UnityCreateView.as_view(), name='add_unity'),
    path('unity_list', views.UnityListView.as_view(), name='unity_list'),
    path('update_unity/<int:pk>', views.UnityUpdateView.as_view(), name='update_unity'),
    path('delete_unity/<int:pk>', views.UnityDeleteView.as_view(), name='delete_unity'),
    path('load_localities/', views.load_localities, name='load_localities'),
    path('load_unities/', views.load_unities, name='load_unities'),
    # city urls
    path('add_city', views.CityCreateView.as_view(), name='add_city'),
    path('city_list', views.CityListView.as_view(), name='city_list'),
    path('update_city/<int:pk>', views.CityUpdateView.as_view(), name='update_city'),
    path('delete_city/<int:pk>', views.CityDeleteView.as_view(), name='delete_city'),
    path('load_cities/', views.load_cities, name='load_cities'),
    # hquarter urls
    path('add_hquarter', views.HquarterCreateView.as_view(), name='add_hquarter'),
    path('hquarter_list', views.HquarterListView.as_view(), name='hquarter_list'),
    path('update_hquarter/<int:pk>', views.HquarterUpdateView.as_view(), name='update_hquarter'),
    path('delete_hquarter/<int:pk>', views.HquarterDeleteView.as_view(), name='delete_hquarter'),
    path('search_state', views.search_state, name='search_state'),
    path('search_locality', views.search_locality, name='search_locality'),
    path('search_hquarter', views.search_hquarter, name='search_hquarter'),
    path('search_unity', views.search_unity, name='search_unity'),
    path('search_city', views.search_city, name='search_city'),
]

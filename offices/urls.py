from django.urls import path
from . import views

app_name = 'offices'
urlpatterns = [
    path('add_hquarter', views.HquarterCreateView.as_view(), name='add_hquarter'),
    path('hquarter_list', views.HquarterListView.as_view(), name='hquarter_list'),
    path('update_hquarter/<int:pk>', views.HquarterUpdateView.as_view(), name='update_hquarter'),
    path('delete_hquarter/<int:pk>', views.HquarterDeleteView.as_view(), name='delete_hquarter'),
    # sector urls
    path('add_sector', views.SectorCreateView.as_view(), name='add_sector'),
    path('sector_list', views.SectorListView.as_view(), name='sector_list'),
    path('update_sector/<int:pk>', views.SectorUpdateView.as_view(), name='update_sector'),
    path('delete_sector/<int:pk>', views.SectorDeleteView.as_view(), name='delete_sector'),
    path('load_hquarters/', views.load_hquarters, name='load_hquarters'),
    # office views
    path('add_office', views.OfficeCreateView.as_view(), name='add_office'),
    path('office_list', views.OfficeListView.as_view(), name='office_list'),
    path('update_office/<int:pk>', views.OfficeUpdateView.as_view(), name='update_office'),
    path('delete_office/<int:pk>', views.OfficeDeleteView.as_view(), name='delete_office'),
    path('load_sectors', views.load_sectors, name='load_sectors'),
    path('load_offices', views.load_offices, name='load_offices'),
    path('search_office', views.search_office, name='search_office'),
]

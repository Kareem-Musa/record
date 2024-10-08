from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('add_range', views.RangeCreateView.as_view(), name='add_range'),
    path('range_list', views.RangeListView.as_view(), name='range_list'),
    path('update_range/<int:pk>', views.RangeUpdateView.as_view(), name='update_range'),
    path('delete_range/<int:pk>', views.RangeDeleteView.as_view(), name='delete_range'),
    # bonus view
    path('add_bonus', views.BonusCreateView.as_view(), name='add_bonus'),
    path('bonus_list', views.BonusListView.as_view(), name='bonus_list'),
    path('update_bonus/<int:pk>', views.BonusUpdateView.as_view(), name='update_bonus'),
    path('delete_bonus/<int:pk>', views.BonusDeleteView.as_view(), name='delete_bonus'),
    # Dgree views
    path('add_dgree', views.DgreeCreateView.as_view(), name='add_dgree'),
    path('dgree_list', views.DgreeListView.as_view(), name='dgree_list'),
    path('update_dgree/<int:pk>', views.DgreeUpdateView.as_view(), name='update_dgree'),
    path('delete_dgree/<int:pk>', views.DgreeDeleteView.as_view(), name='delete_dgree'),
    # employee views
    path('add_employee', views.add_employee, name='add_employee'),
    path('update_employee/<int:pk>', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('employee_list', views.EmployeeListView.as_view(), name='employee_list'),
    path('load_current_localities/', views.load_current_localities, name='load_current_localities'),
    path('load_current_unities/', views.load_current_unities, name='load_current_unities'),
    # search Employee
    path('search_employee', views.search_employee, name='search_employee'),
    # document urls
    path('add_document', views.create_document, name='create_document'),
    path('document_list', views.DocumentListView.as_view(), name='document_list'),
    path('EmployeeAutocomplete', views.EmployeeAutocomplete.as_view(), name='EmployeeAutocomplete'),
]

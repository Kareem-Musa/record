from django.urls import path
from . import views

app_name  = 'departments'
urlpatterns = [
    path('add_planning', views.PlanningCreateView.as_view(), name='add_planning'),
    path('planning_list', views.PlanningListView.as_view(), name='planning_list'),
    path('update_planning/<int:pk>', views.PlanningUpdateView.as_view(), name='update_planning'),
    path('delete_planning/<int:pk>', views.PlanningDeleteView.as_view(), name='delete_planning'),
    # Department urls
    path('add_department', views.DepartmentCreateView.as_view(), name='add_department'),
    path('department_list', views.DepartmentListView.as_view(), name='department_list'),
    path('update_department/<int:pk>', views.DepartmentUpdateView.as_view(), name='update_department'),
    path('delete_department/<int:pk>', views.DepartmentDeleteView.as_view(), name='delete_department'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PlanListView.as_view(), name='plan-list'),
    path('create/', views.PlanCreateView.as_view(), name='plan-create'),
    path('delete/<int:id>/', views.PlanDeleteView.as_view(), name='plan-delete'),
]

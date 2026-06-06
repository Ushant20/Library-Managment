from django.urls import path
from .views import (
    StudentListCreateView,
    DashboardView,
    LoginView,
    StudentDetailView,
    PaymentListCreateView,
    PaymentStatsView,
    SettingsView
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('dashboard/', DashboardView.as_view()),
    path('login/', LoginView.as_view()),
path(
    'students/<int:pk>/',
    StudentDetailView.as_view(),
    name='student-detail'
),
path(
    "payments/",
    PaymentListCreateView.as_view()
),
path(
    "payment-stats/",
    PaymentStatsView.as_view()
),
path(
    "settings/",
    SettingsView.as_view()
),
]
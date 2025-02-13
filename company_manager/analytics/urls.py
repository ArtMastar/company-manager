from django.urls import path
from .views import analytics_dashboard

app_name = 'analytics'

urlpatterns = [
    path('', analytics_dashboard, name='dashboard'),
]

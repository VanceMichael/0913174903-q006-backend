from django.urls import path

from app.main import HealthView

urlpatterns = [path("health", HealthView.as_view())]

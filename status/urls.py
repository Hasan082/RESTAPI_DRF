from django.urls import path
from .views import StatusView


urlpatterns = [
    path('all/', StatusView.as_view(), name='status_list'),
]

from django.urls import path
from status.views import StatusView


urlpatterns = [
    path('status/<id:str>/', StatusView.as_view(), name='status_list'),
]

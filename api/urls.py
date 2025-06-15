from django.urls import path
from status.views import StatusView


urlpatterns = [
    path('status/', StatusView.as_view(), name='status_list'),
    path('status/<int:id>/', StatusView.as_view(), name='status_single'),
]


# List, Create API View (Part 1)
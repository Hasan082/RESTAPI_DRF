from django.urls import path
from status.views import StatusView, StatusListView


urlpatterns = [
    path('status/', StatusListView.as_view()),
    path('status/<int:id>/', StatusView.as_view()),
]


# List, Create API View (Part 1)
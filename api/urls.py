from django.urls import path
from status.views import (StatusView, StatusListView, StatusCreateView, 
                          StatusDetailsView, StatusUpdateView, StatusDeleteView)


urlpatterns = [
    # path('status/', StatusListView.as_view()), # USED APIVIEW
    
    path('status/', StatusListView.as_view()), # Extends APIview to generic
    path('status/<int:id>/', StatusView.as_view()),
    path('status/create/', StatusCreateView.as_view()),
    path('status/details/<int:pk>/', StatusDetailsView.as_view()),
    path('status/update/<int:pk>/', StatusUpdateView.as_view()),
    path('status/delete/<int:pk>/', StatusDeleteView.as_view()),
]


# List, Create API View (Part 1)
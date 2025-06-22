from django.urls import path

# FOR MIXINS FOR CRUD OPERATIONS
from status.views import StatusListCreateView, StatusDetailUpdateDestroyView


# USING GENRAL WAY AND GENRIC VIEWS FOR CRUD OPERATIONS
# from status.views import (StatusView, StatusListView, StatusCreateView, 
#                           StatusDetailsView, StatusUpdateView, StatusDeleteView)




urlpatterns = [
    # USING MIXINS FOR CRUD OPERATIONS
    path('status/', StatusListCreateView.as_view()),  # List and Create
    path('status/<int:pk>', StatusDetailUpdateDestroyView.as_view()),  # WITH PK for Get, Put, Patch, Delete
    
    
    # USING GENERICS FOR CRUD OPERATIONS
    # path('status/', StatusListView.as_view()), 
    # path('status/<int:id>/', StatusView.as_view()),
    # path('status/create/', StatusCreateView.as_view()),
    # path('status/details/<int:pk>/', StatusDetailsView.as_view()),
    # path('status/update/<int:pk>/', StatusUpdateView.as_view()),
    # path('status/delete/<int:pk>/', StatusDeleteView.as_view()),
]


# List, Create API View (Part 1)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer


# MAKE API VIEWS USING GENERICS AND MIXINS

# ListCreateAPIView
#     ├── CreateModelMixin (for POST)
#     ├── ListModelMixin (for GET)
#     └── GenericAPIView (base view logic)


class StatusListCreateView(generics.ListCreateAPIView, mixins.CreateModelMixin):
    """
    Handle GET and POST requests for status entries.
    This view allows users to retrieve a list of all statuses or create a new status.
    Example:
        GET /api/status/ - Retrieve all statuses
        POST /api/status/ - Create a new status
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = (
        StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer'
    )

    # POST requests to create a new status.
    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)


class StatusDetailUpdateDestroyView(
    generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    """
    Handle GET, PUT, PATCH, and DELETE requests for a specific status.
    This view allows users to retrieve, update, or delete a status entry by its primary key (pk).
    Example:
        GET /api/status/detail/1/ - Retrieve status with ID 1
        PUT /api/status/update/1/ - Update status with ID 1
        PATCH /api/status/update/1/ - Partially update status with ID 1
        DELETE /api/status/delete/1/ - Delete status with ID 1
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = (
        StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer'
    )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs): 
        return self.partial_update(request, *args, **kwargs)



# GENERAL WAY TO MAKE API VIEWS

# Way 1
# class StatusListView(APIView):
#     """
#     Handle GET requests to retrieve all statuses.

#     This view returns a list of all status entries from the database.
#     It uses the StatusSerializer to serialize the data.

#     Example:
#         GET /api/status/
#     """

#     def get(self, request):
#         """
#         Retrieve all status objects.

#         Args:
#             request: The HTTP request object.

#         Returns:
#             Response: A list of serialized status data.
#         """
#         all_status = Status.objects.all()
#         serializer = StatusSerializer(all_status, many=True)
#         return Response(serializer.data)


class StatusView(APIView):
    """
    Handle GET requests to retrieve a single status by ID.

    This view returns the status object corresponding to the given ID.
    If the status is not found, a 404 error is automatically raised.

    Example:
        GET /api/status/1/
    """

    def get(self, request, id):
        """
        Retrieve a specific status by its ID.

        Args:
            request: The HTTP request object.
            id (int): The ID of the status to retrieve.

        Returns:
            Response: Serialized status data.

        Raises:
            Http404: If no Status object with the given ID exists.
        """
        status = get_object_or_404(Status, pk=id)
        serializer = StatusSerializer(status)
        return Response(serializer.data)


# List, Create API View (Part 2)


class StatusListView(generics.ListAPIView):
    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer' or any other variation


class StatusCreateView(generics.CreateAPIView):
    """
    Handle POST requests to create a new status.

    This view allows users to create a new status entry in the database.
    It uses the StatusSerializer to validate and save the data.

    Example:
        POST /api/status/
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer' or any other variation


class StatusDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handle GET, PUT, PATCH, and DELETE requests for a specific status.

    This view allows users to retrieve, update, or delete a status entry
    by its primary key (pk). It uses the StatusSerializer for serialization.

    Example:
        GET /api/status/detail/1/
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer' or any other variation


class StatusUpdateView(generics.UpdateAPIView):
    """
    Handle PUT and PATCH requests to update a specific status.

    This view allows users to update an existing status entry by its primary key (pk).
    It uses the StatusSerializer for serialization.

    Example:
        PUT /api/status/update/1/
        PATCH /api/status/update/1/
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer' or any other variation


class StatusDeleteView(generics.DestroyAPIView):
    """
    Handle DELETE requests to remove a specific status.

    This view allows users to delete a status entry by its primary key (pk).
    It uses the StatusSerializer for serialization.

    Example:
        DELETE /api/status/delete/1/
    """

    queryset = (
        Status.objects.all()
    )  # MUST BE WORD 'queryset' NOT 'query_set' or any other variation
    serializer_class = StatusSerializer  # MUST BE WORD 'serializer_class' NOT 'serializer' or any other variation

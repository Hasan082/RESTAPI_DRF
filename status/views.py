from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer


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


class StatusListView(APIView):
    """
    Handle GET requests to retrieve all statuses.

    This view returns a list of all status entries from the database.
    It uses the StatusSerializer to serialize the data.

    Example:
        GET /api/status/
    """

    def get(self, request):
        """
        Retrieve all status objects.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A list of serialized status data.
        """
        all_status = Status.objects.all()
        serializer = StatusSerializer(all_status, many=True)
        return Response(serializer.data)

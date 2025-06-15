from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status

from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
    
class StatusView(APIView):
    
    def get(self, request, id=None):
        """
        Handle GET requests to retrieve all statuses.
        """
        if id:
            try:
                status = get_object_or_404(Status, pk=id)
                serializer = StatusSerializer(status)
                return Response(serializer.data)
            except FileNotFoundError as e:
                print("Not found ID")
        else:
            all_status = Status.objects.all()
            serializer = StatusSerializer(all_status, many=True)
            return Response(serializer.data)
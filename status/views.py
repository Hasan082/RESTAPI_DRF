from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer



class StatusView(APIView):
    def get(self, request):
        """
        Handle GET requests to retrieve all statuses.
        """
        all_status = Status.objects.all()
        serializer = StatusSerializer(all_status, many=True)
        return Response(serializer.data)
    
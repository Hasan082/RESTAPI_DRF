from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from status.models import Status
from status.serializers import StatusSerializer

class StatusView(APIView):

    # GET: retrieve one or all
    def get(self, request, id=None):
        if id:
            status_obj = get_object_or_404(Status, pk=id)
            serializer = StatusSerializer(status_obj)
        else:
            statuses = Status.objects.all()
            serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)

    # POST: create new
    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT: full update
    def put(self, request, id):
        status_obj = get_object_or_404(Status, pk=id)
        serializer = StatusSerializer(status_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: partial update
    def patch(self, request, id):
        status_obj = get_object_or_404(Status, pk=id)
        serializer = StatusSerializer(status_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: remove an object
    def delete(self, request, id):
        status_obj = get_object_or_404(Status, pk=id)
        status_obj.delete()
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

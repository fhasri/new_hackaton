from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]  # Set appropriate permissions

    def create(self, request, *args, **kwargs):
        # Add logic for creating feedback
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        feedback = serializer.save(user=request.user)
        return Response(serializer.data, status=201)

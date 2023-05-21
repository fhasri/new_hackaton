
from rest_framework import viewsets
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer , CommentFilterSet
from apps.product.permissions import IsOwnerPermission, IsAdminOrActivePermission, AllowAny

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_class = CommentSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CommentFilterSet 

    def get_permissions(self):
        if self.action in ['update', 'destroy', 'partial_update']:
            self.permission_classes = [IsOwnerPermission]
        elif self.action == 'create':
            self.permission_classes = [IsAdminOrActivePermission]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

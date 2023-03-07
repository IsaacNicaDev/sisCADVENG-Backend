from rest_framework import viewsets, permissions

from .models import Group
from .serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupSerializer



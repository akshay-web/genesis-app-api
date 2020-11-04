from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from genesis.permissions import CustomDjangoModelPermissions
from django.db.models import Q

from projectmgmt.models import Project

from projectmgmt import serializers

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [CustomDjangoModelPermissions,]

    def get_queryset(self):
        """Retrieve the projects for the authenticated user"""
        users = self.request.query_params.get('users')
        title = self.request.query_params.get('title')
        description = self.request.query_params.get('description')
        status = self.request.query_params.get('status')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        search = self.request.query_params.get('search')
        queryset = self.queryset

        lookups = Q(users__username__icontains=search) | Q(title__icontains=search) | \
                  Q(description__icontains=search) | Q (status__icontains=search) | \
                  Q(start_date__icontains=search) | Q(end_date__icontains=search)

        if search:
            queryset = queryset.filter(lookups).distinct()
            
        if users:
            queryset = queryset.filter(users__username__icontains=users)

        if title:
            queryset = queryset.filter(title__icontains=title)

        if description:
            queryset = queryset.filter(description__icontains=description)
        
        if status:
            queryset = queryset.filter(status__icontains=status)

        if start_date:
            queryset = queryset.filter(start_date=start_date)

        if end_date:
            queryset = queryset.filter(end_date=end_date)

        return queryset

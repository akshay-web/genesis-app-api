from rest_framework import serializers

from projectmgmt.models import Project, User

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project objects"""
    users = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Project
        fields = ('id', 'users', 'title', 'description', 'status', 'start_date', 'end_date')
        read_only_fields = ('id',)
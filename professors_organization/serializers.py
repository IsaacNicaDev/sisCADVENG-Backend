from rest_framework import serializers

from .models import Group



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "grade_id", "academic_year","guide_professor_id","created_at", "updated_at")
        read_only_fields = ("created_at",)



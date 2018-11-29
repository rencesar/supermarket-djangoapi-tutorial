from rest_framework import serializers
from .models import Section


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('name', 'max_allowed_items', 'description', 'temperature')

from rest_framework import serializers

from core.models import Ingredient, Data


class DataIngestionSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Data
        fields = ('id', 'name', 'Object_file', 'Development_data', 'Monitoring_data')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

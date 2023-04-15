from rest_framework import serializers
from .models import LinkedinPost
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedinPost
        fields = '__all__'
    
    def create(self, validated_data):
        return super().create(validated_data)
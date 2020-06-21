from rest_framework import serializers
from .models import Realtor


class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realtor
        # fields = ['name', 'photo', 'description', 'email', 'phone', 'message', 'is_mvp', 'contact_date']
        fields = '__all__'

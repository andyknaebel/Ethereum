from rest_framework import serializers
from .models import employee

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'First', 'Last', 'url']
        #fields = '__all__'
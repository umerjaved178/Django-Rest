from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Bookmodel

class PostSerializers(serializers.ModelSerializer):
    
    class Meta:
        fields=('id','title','author','description')
        model=Bookmodel
        
class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
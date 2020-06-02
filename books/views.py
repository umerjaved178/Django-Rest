from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Bookmodel

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializers, UserSerializer 

# Create your views here.
class List(generics.ListCreateAPIView):
    queryset=Bookmodel.objects.all()
    serializer_class=PostSerializers
    
class Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset=Bookmodel.objects.all()
    serializer_class=PostSerializers
    
class UserList(generics.ListCreateAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
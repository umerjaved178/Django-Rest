from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Bookmodel

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializers, UserSerializer 


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Bookmodel.objects.all()
    serializer_class = PostSerializers

    
class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
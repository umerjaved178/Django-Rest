from django.urls import path
from .views import Detail,List,UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('<int:pk>/',Detail.as_view()),
    path('',List.as_view()),
]
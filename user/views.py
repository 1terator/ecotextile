from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .permissions import IsCurrentUser
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, MiniUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = MiniUserSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated & IsCurrentUser])
    def me(self, request, pk=None):
        serializer_class = self.get_serializer_class()
        instance = get_object_or_404(User.objects.filter(id=request.user.id))
        serializer = serializer_class(instance=instance)
        return Response(serializer.data)


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import *
from rest_framework.permissions import *
from .models import *
from .serializers import * 
from .permissions import IsAuthenticatedAndOwner
# Create your views here.

class TrainerView(ModelViewSet):
    serializer_class = TrainerSerailizer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Trainer.objects.all()
        else:
            user_id = self.request.user.id
            if user_id:
                return Trainer.objects.filter(user_id=user_id)

    def get_permissions(self):
        if self.action in ['list','retrieve','create']:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticatedAndOwner()]

    def get_serializer_context(self):
        context = super(TrainerView, self).get_serializer_context()
        context["user_id"] = self.request.user.id
        context["user_type"] = self.request.user.user_type

        print(context["user_id"],context["user_type"])
        return context

class ClientView(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        else:
            user_id = self.request.user.id
            if user_id:
                return Client.objects.filter(user_id=user_id)

    def get_permissions(self):
        if self.action in ['list','retrieve','create']:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticatedAndOwner()]

    def get_serializer_context(self):
        context = super(ClientView,self).get_serializer_context()
        context["user_id"] = self.request.user.id
        context["user_type"] = self.request.user.user_type

        return context


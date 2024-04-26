from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from django.db.models import Prefetch,Subquery
from rest_framework import mixins
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from .models import Muscle,TrainingFocus,Plan,Day,Exercise,Plan_Day,Plan_Day_Exercise,Plan_Day
from . import models
from .serializers import MuscleSerializer,TrainingFocusSerializer
from . import serializers
from rest_framework.permissions import IsAuthenticated
from . import permissions

###################################################################

class BaseViewSet(RetrieveModelMixin,ListModelMixin, GenericViewSet):
    pass

class BaseEditViewSet(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    pass

###################################################################

class MusclesList(BaseViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer

###################################################################

class TrainingFocusList(BaseViewSet):

    queryset = TrainingFocus.objects.prefetch_related('muscle').all()
    serializer_class = TrainingFocusSerializer

###################################################################

class TraineeCreateView(mixins.CreateModelMixin,GenericViewSet):

    queryset = models.Trainee.objects.all()
    serializer_class = serializers.TraineeSerializer
    permission_classes = [IsAuthenticated]

###################################################################

class TraineeUpdateView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,GenericViewSet):

    queryset = models.Trainee.objects.all()
    serializer_class = serializers.TraineeSerializer

    def get_permissions(self):
        print(self.action)
        if self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAuthenticatedAndOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
###################################################################

class PlanList(BaseViewSet,BaseEditViewSet):

    permission_classes = [permissions.CustomPermission]
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PATCH','PUT']:
            print("Ok")
            return serializers.CreateUpdatePlanSerializer
        else:
            return serializers.PlanSerializer

    def get_queryset(self):
        try:
            training_focus_id = self.kwargs['trainingfocus_pk']
        except:
            training_focus_id = None
            
        if training_focus_id:
            queryset = queryset.filter(training_focus_id=training_focus_id)
        queryset = Plan.objects.all()

        queryset = queryset.select_related('training_focus').prefetch_related('plan_rel__day').prefetch_related('plan_rel__plan_day_rel__exercise')
        return queryset
###################################################################

class DayList(BaseViewSet):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer

###################################################################

class ExerciseList(BaseViewSet,BaseEditViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer
    permission_classes = [permissions.CustomPermission]

##################################################################

class MainAdviceList(BaseViewSet,BaseEditViewSet):
    queryset = models.MainAdvice.objects.prefetch_related('sub_advices').all()
    serializer_class = serializers.MainAdviceSerializer
    permission_classes = [permissions.CustomPermission]

##################################################################

class SubAdviceList(BaseViewSet,BaseEditViewSet):
    queryset = models.SubAdvice.objects.all()
    serializer_class = serializers.SubAdviceSerializer
    permission_classes = [permissions.CustomPermission]

##################################################################
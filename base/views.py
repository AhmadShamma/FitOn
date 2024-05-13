from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import *
from .permissions import * 
from .serializers import *
from .models import *
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

class TrainingFocusList(BaseViewSet,BaseEditViewSet):

    queryset = TrainingFocus.objects.prefetch_related('muscle').all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return CreateUpdateTrainingFocusSerializer
        return TrainingFocusSerializer
    
###################################################################

class PlanList(BaseViewSet,BaseEditViewSet):

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateUpdatePlanSerializer
        return PlanSerializer

    # permission_classes = [permissions.CustomPermission]
    def get_queryset(self):
        try:
            training_focus_id = self.kwargs['trainingfocus_pk']
        except:
            training_focus_id = None
        queryset = Plan.objects.all().order_by('id')
        if training_focus_id:
            queryset = queryset.filter(training_focus_id=training_focus_id)

        queryset = queryset.select_related('training_focus').prefetch_related('plan_rel__day').prefetch_related('plan_rel__plan_day_rel__exercise')
        return queryset
###################################################################

class DayList(BaseViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

###################################################################

class ExerciseList(BaseViewSet,BaseEditViewSet):
    queryset = Exercise.objects.all().order_by('id')
    serializer_class = ExerciseSerializer
    # permission_classes = [permissions.CustomPermission]

################################################################

class MainAdviceList(BaseViewSet,BaseEditViewSet):
    queryset = MainAdvice.objects.prefetch_related('sub_advices').all().order_by('id')
    # permission_classes = [permissions.CustomPermission]

    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return CreateUpdateMainAdviceSerializer
        return MainAdviceSerializer

##################################################################

class SubAdviceList(BaseViewSet,BaseEditViewSet):
    queryset = SubAdvice.objects.all()
    serializer_class = SubAdviceSerializer
    # permission_classes = [CustomPermission]

##################################################################



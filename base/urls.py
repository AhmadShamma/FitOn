from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views
from core.views import *
#####################################################

router = DefaultRouter()
router.register('muscles',views.MusclesList,basename='muslces')
router.register('trainingfocus',views.TrainingFocusList,basename='trainingfocus')
router.register('advice',views.MainAdviceList,basename='advice')
router.register('plan',views.PlanList,basename='plan')
router.register('exercise',views.ExerciseList,basename='exercise')


trainingfocus_router = DefaultRouter()
trainingfocus_router.register('trainingfocus',views.TrainingFocusList,basename='trainingfocus')

Plan_nested_router = routers.NestedDefaultRouter(trainingfocus_router,'trainingfocus',lookup='trainingfocus')
Plan_nested_router.register('plan',views.PlanList,basename='plan')


urlpatterns = [
    path('',include(router.urls)),
    path('',include(trainingfocus_router.urls)),
    path('',include(Plan_nested_router.urls)),
    
]
from rest_framework import serializers
from .models import *
###############################################################

class MuscleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        fields = ['id','name','image']
        model = Muscle

###############################################################

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name']
        model = Day

###############################################################

class ExerciseSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()
    video = serializers.FileField()

    class Meta:
        fields = ['id','name','description','reps','sets','image','video']
        model = Exercise

###############################################################

class SimpleMuscleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name']
        model = Muscle

###############################################################

class TrainingFocusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    muscle = SimpleMuscleSerializer(many=True)
    image = serializers.ImageField()

    class Meta:
        fields = ['id','name','level','description','image','muscle']
        model = TrainingFocus

###############################################################

class SimpleTrainingFocusSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        fields = ['name']
        model = TrainingFocus

    def get_name(self,obj):
        return obj.name


###############################################################

class PlanDayExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    class Meta:
        fields = ['exercise']
        model = Plan_Day_Exercise
    
###############################################################

class PlanDaySerializer(serializers.ModelSerializer):
    day_name = serializers.SerializerMethodField()
    exercises = serializers.SerializerMethodField()
    class Meta:
        fields = ['day_name','exercises']
        model = Plan_Day

    def get_day_name(self,obj):
        return obj.day.name
    
    def get_exercises(self,obj):
        return [
            {
                'id' : exercise.exercise.id,
                'name':exercise.exercise.name,
                'description' : exercise.exercise.description,
                'sets' : exercise.exercise.sets,
                'reps' : exercise.exercise.reps,
                'image': exercise.exercise.image.url if exercise.exercise.image else None,
                'video': exercise.exercise.video.url if exercise.exercise.video else None
                
            }
            for exercise in obj.plan_day_rel.all()
        ]
    
###############################################################

class PlanSerializer(serializers.ModelSerializer):
    training_focus = serializers.SerializerMethodField()
    plan_detail = PlanDaySerializer(source='plan_rel',many=True)
    class Meta:
        fields = ['id','advice','weeks','training_focus','image','plan_detail']
        model = Plan

    def get_training_focus(self,obj):
        return obj.training_focus.name
###############################################################

class SubAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','title','description']
        model = SubAdvice

###############################################################

class MainAdviceSerializer(serializers.ModelSerializer):
    sub_advices = SubAdviceSerializer(many=True)
    image = serializers.ImageField()
    class Meta:
        fields = ['id','title','description','image','sub_advices']
        model = MainAdvice

###############################################################


class CreateUpdatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','advice','weeks','training_focus','image']
        model = Plan

###############################################################

class CreateUpdateMainAdviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','title','description','image']
        model = MainAdvice

###############################################################

class CreateUpdateTrainingFocusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name','description','level','image']
        model = TrainingFocus

###############################################################


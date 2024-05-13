from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import *
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','email','password','first_name','last_name','user_type']


class TrainerSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = [
            'id' , 'birth_date',
            'phone_number', 'gender', 'bio', 'specialities',
            'experience_years', 'is_available', 'working_hours',
            'instagram_profile', 'twitter_profile', 'linkedin_profile',
        ]

    def create(self, validated_data):
        if self.context.get("user_type") == 'Cl':
            raise ValidationError("This User Can only create a Trainer account")
        else:
            return Trainer.objects.create(user_id=self.context.get('user_id'),**validated_data)

###############################################################

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id', 'birth_date', 'phone_number', 'gender',
            'height', 'weight', 'health_conditions',
            'fitness_goals', 'sessions_completed', 'progress_notes'
        ]
    def create(self, validated_data):
        user_id = self.context.get("user_id")
        if self.context.get("user_type") == 'TR':
            raise ValidationError("This user can only create a trainee account")
        else:
            return Client.objects.create( user_id = user_id ,**validated_data)
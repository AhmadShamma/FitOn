from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,EmailValidator
from . import validators
from django.conf import settings
from django.db.models import Q,F,CheckConstraint
from django.utils import timezone
import re
# Create your models here.

def Validator_Email(email:str) :
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.com$)")
    if re.fullmatch(pattern,email) is None:
        raise ValidationError("Please enter a valid Email")

def phone_number_validator(value):
    pattern = re.compile(r"^\+?1?\d{9,15}$")
    if re.fullmatch(pattern,value) is None:
        raise ValidationError("Invalid phone number. Please enter a number that is 9 to 15 digits long and may start with '+'.")

def validate_height(height):
    if height <= 0 or height >= 272 :
        raise ValidationError("Please enter a valid height bigger than zero and less than 272 in centimeters")
    
def validate_weight(weight):
    if weight <= 0 or weight >= 635 :
        raise ValidationError("Please enter a valid weight bigger than zero and less than 635 in kilogram ")
        
def validate_birth_date(birth_date):
    if birth_date > timezone.now().date():
        raise ValidationError("Please enter a valid birth date - Birth date can't be in the future")

def validate_session_completed(session_completed):
    if session_completed < 0 :
        raise ValidationError("Please enter a valid session_completed - session_completed should be a positive number")

class UserTypes(models.TextChoices):
    Trainer = 'TR','Trainer'
    Client = 'CL','Client'

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

class User(AbstractUser):

    username = models.CharField(max_length=150,blank=False,unique=True)
    email = models.EmailField(unique=True,blank=False)
    user_type = models.CharField(choices = UserTypes.choices,default = UserTypes.Client)


    def save(self,*args,**kwargs):
        if self.user_type == UserTypes.Client:
            Validator_Email(self.email)
        else:
            EmailValidator(self.email)
        return super().save(*args,**kwargs)

class Client(models.Model):

    birth_date = models.DateField(blank=True,null=True,validators=[validate_birth_date])
    phone_number = models.CharField(max_length=15,blank=True,null=True,validators=[phone_number_validator])
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='M')


    height = models.DecimalField(max_digits=5, decimal_places=2,validators=[validate_height])
    weight = models.DecimalField(max_digits=5, decimal_places=2,validators=[validate_weight])
    health_conditions = models.TextField(blank=True,null=True)

    fitness_goals = models.TextField(blank=True,null=True)

    sessions_completed = models.PositiveIntegerField(default=0,blank=True,null=True)
    progress_notes = models.TextField(blank=True,null=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(gender='M') | Q(gender='F'),
                name = 'Check_Client_Gender'
            )
        ]
    
##################################################################


class Trainer(models.Model):

    birth_date = models.DateField(blank=True,null=True,validators=[validate_birth_date])
    phone_number = models.CharField(max_length=15,blank=True,null=True,validators=[phone_number_validator])
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='M')

    height = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True,validators=[validate_height])
    weight = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True,validators=[validate_weight])
    bio = models.TextField(blank=True,null=True)
    specialities = models.CharField(max_length=200) 
    experience_years = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)
    working_hours = models.CharField(max_length=100) 

    instagram_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(gender='M') | Q(gender='F'),
                name = 'Check_Trainee_Gender'
            )
        ]




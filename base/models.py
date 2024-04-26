from django.db import models
from django.core.validators import URLValidator
from FitOn.settings import AUTH_USER_MODEL

######################################################################

class Muscle(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='base/images',blank=True,null=True)

    def str(self):
        return self.name
    
######################################################################

class TrainingFocus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    level = models.SmallIntegerField(default=1,help_text='The difficulty level of the plan type.')
    description = models.TextField()
    muscle = models.ManyToManyField(Muscle)
    image = models.ImageField(upload_to='base/images',blank=True,null=True)

    def str(self):
        return self.name
    
    class Meta:
        ordering = ['level', 'id']

######################################################################

class Exercise(models.Model):  
    name = models.CharField(max_length=255)
    description = models.TextField()
    sets = models.PositiveSmallIntegerField()
    reps = models.CharField(max_length=255)
    image = models.ImageField(upload_to='base/images',blank=True,null=True)
    video = models.FileField(upload_to='base/videos',blank=True,null=True)

    def __str__(self):
        return self.name

######################################################################

class Day(models.Model):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name
    
######################################################################

class Plan(models.Model):
    advice = models.TextField(null=True,blank=True)
    weeks = models.SmallIntegerField()
    day = models.ManyToManyField(Day,through='Plan_Day')
    training_focus = models.ForeignKey(TrainingFocus, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='base/images',blank=True,null=True)

    def str(self):
        return self.name
    
######################################################################

class Plan_Day(models.Model):
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='plan_rel')
    day = models.ForeignKey(Day,on_delete=models.CASCADE,related_name='day_rel')
    exercise = models.ManyToManyField(Exercise,through='Plan_Day_Exercise')

    class Meta:
        unique_together = ('plan','day')

######################################################################

class Plan_Day_Exercise(models.Model):
    plan_day = models.ForeignKey(Plan_Day,on_delete=models.CASCADE,related_name='plan_day_rel')
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,related_name='exercise_rel')

    class Meta:
        unique_together = ('plan_day','exercise')
######################################################################

class Trainee(models.Model):
    birth_date = models.DateField(blank=True,null=True)

    phone_number = models.CharField(max_length=15,blank=True,null=True)

    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    health_conditions = models.TextField(blank=True)

    fitness_goals = models.TextField(blank=True)

    sessions_completed = models.PositiveIntegerField(default=0,blank=True)
    progress_notes = models.TextField(blank=True)

    user = models.OneToOneField(
        AUTH_USER_MODEL,on_delete=models.CASCADE
    )

##################################################################

class MainAdvice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='base/images',blank=True,null=True)

    def __str__(self):
        return self.title
    
##################################################################

class SubAdvice(models.Model):
    main_advice = models.ForeignKey(MainAdvice, related_name='sub_advices', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

##################################################################

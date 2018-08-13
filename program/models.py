from django.db import models

# Create your models here.

class Week(models.Model):
	week_number = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=None)
	start_date = models.DateField()
	metric = models.IntegerField() # enum 
	bench_press_max = models.IntegerField()
	squat_max = models.IntegerField()
	deadlift_max = models.IntegerField() 
	upper_back_exercise = models.IntegerField() # enums??
	upper_back_exercise_2 = models.IntegerField()
	shoulder_exercise = models.IntegerField()

class Day(models.Model):
	week_number = models.ForeignKey(Week, on_delete=models.CASCADE)
	focus = models.IntegerField() # enum
	day = models.CharField(max_length=None)
	date = models.DateField()

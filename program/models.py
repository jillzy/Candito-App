from django.db import models

# Create your models here.

class Week(models.Model):
	week_number = models.IntegerField(primary_key=True)
	start_date = models.DateField()
	metric = models.IntegerField() # enum 
	bench_press_max = models.IntegerField()
	squat_max = models.IntegerField()
	deadlift_max = models.IntegerField()
	upper_back_exercise = 
	upper_back_exercise_2 =
	shoulder_exercise =
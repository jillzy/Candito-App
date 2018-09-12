from django.db import models

# Create your models here.
class Profile(models.Model):
	metric = models.IntegerField() # enum 
	program_start = CharField(max_length=50)
	bench_press_max = models.IntegerField()
	squat_max = models.IntegerField()
	deadlift_max = models.IntegerField()
	upper_back_exercise = models.CharField(max_length=25) # enums??
	upper_back_exercise_2 = models.CharField(max_length=25)
	shoulder_exercise = models.CharField(max_length=25)

	def update_metric(self, val):
		metric = val

	def update_program_start(self, val):
		program_start = val

	def update_bench_max(self, val):
		self.bench_press_max = val

	def update_squat_max(self, val):
		self.squat_max = val

	def update_deadlift_max(self, val):
		self.deadlift_max = val

	def update_upper_back_ex(self, val):
		self.upper_back_exercise = val

	def update_upper_back_ex2(self, val):
		self.upper_back_exercise_2 = val

	def update_shoulder_ex(self, val):
		self.shoulder_exercise = val


class Week(models.Model):
	week = models.IntegerField(primary_key=True)
	number_of_days = models.IntegerField()
	phase = models.CharField(max_length=50)

class Day(models.Model):
	week = models.ForeignKey(Week, on_delete=models.CASCADE)
	day = models.CharField(max_length=25)

class Exercise(models.Model):
	name = models.CharField(max_length=25)
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	weight = models.IntegerField()
	reps = models.IntegerField()
	sets = models.IntegerField()

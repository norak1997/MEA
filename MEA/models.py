from django.db import models
from django.utils import timezone

class Questions(models.Model):

	category = models.CharField(max_length=200)
	question = models.CharField(max_length=1000)
	op1 = models.CharField(max_length=200)
	op2 = models.CharField(max_length=200)
	op3 = models.CharField(max_length=200)
	op4 = models.CharField(max_length=200)
	types = (('Option1',op1),('Option2',op2),('Option3',op3),('Option4',op4))
	correct = models.CharField(max_length = 30,choices = types,blank=False)

	def __str__(self):
		return self.category+self.question

class Placement(models.Model):
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name

class Events(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='events')
	description = models.TextField()

	def __str__(self):
		return self.name

class Projects(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='projects')
	description = models.TextField()

	def __str__(self):
		return self.name

class Resources(models.Model):
	name = models.CharField(max_length=200)
	file = models.FileField(upload_to='resources')

	def __str__(self):
		return self.name




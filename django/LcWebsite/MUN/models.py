from django.db import models

COMM_CHOICES = (
    ('C1','United Nations General Assembly - DISEC'),
    ('C2', 'The All India Oppostion Meet'),
    ('IPJ','International Press Journalist'),
    ('IPP', 'International Press Photographer'),
    
)



class FormNew(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	number = models.CharField(max_length=15, default='0123456789')
	committee = models.CharField(max_length=20, choices=COMM_CHOICES, default='C1')
	college = models.CharField(max_length=200, default='NITD')
	#category = models.ChoiceField()
	#Committee= models.CharField(max_length=300)
	Past_Experience = models.CharField(max_length=1000,default='None')
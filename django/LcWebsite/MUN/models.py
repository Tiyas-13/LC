from django.db import models

COMM_CHOICES = (
    ('C1','United Nations General Assembly - DISEC'),
    ('C2', 'The All India Oppostion Meet'),
    
    )

IP_CHOICES = (
	('IPJ','International Press Journalist'),
    ('IPP', 'International Press Photographer'),
	)


class CommitteeNew(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	number = models.CharField(max_length=15, default='0123456789')
	committee = models.CharField(max_length=20, choices=COMM_CHOICES, default='C1')
	college = models.CharField(max_length=200, default='NITD')
	Past_Experience = models.CharField(max_length=1000,default='None')
	preference1 = models.CharField(max_length=150, default= 'None')
	preference2 = models.CharField(max_length=150, default= 'None')
	preference3 = models.CharField(max_length=150, default= 'None')

class IPNew(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField()
	number = models.CharField(max_length=15, default='0123456789')
	Choice = models.CharField(max_length=20, choices=IP_CHOICES, default='IPJ')
	college = models.CharField(max_length=200, default='NITD')
	Past_Experience = models.CharField(max_length=1000,default='None')
	preference1 = models.CharField(max_length=150, default= 'None')
	preference2 = models.CharField(max_length=150, default= 'None')
	preference3 = models.CharField(max_length=150, default= 'None')
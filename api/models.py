from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    number = models.CharField(max_length=100, blank=False)
    rollno = models.CharField(max_length=100, blank=False)
    hallno = models.CharField(max_length=100, blank=False)
    section = models.CharField(max_length=100, blank=False)
    club_preference = models.CharField(max_length=300, blank=False)
    roles_preference = models.CharField(max_length=300, blank=False)
    answer_1_text = models.TextField(max_length=1000, blank=False)
    answer_2_text = models.TextField(max_length=1000, blank=False)
    answer_3_text = models.TextField(max_length=1000, blank=False)
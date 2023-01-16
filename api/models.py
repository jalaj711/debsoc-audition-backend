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
    answer_1_text = models.TextField(
        verbose_name="Rate yourself(out of 10, 1 being lowest and 10 highest) in the following", max_length=1000)
    answer_2_text = models.TextField(verbose_name="You get a wish to travel back in time, what is that one mistake you want to correct?", max_length=1000)
    answer_3_text = models.TextField(verbose_name="Why should Shizuka choose Gian over other characters?", max_length=1000)
    answer_4_text = models.TextField(verbose_name="Hunter or gatherer?", max_length=1000)
    answer_5_text = models.TextField(verbose_name="Any advice for your previous self?", max_length=1000)
    answer_6_text = models.TextField(verbose_name="If you were given a box of markers, what would you do with them that are not their traditional use.", max_length=1000)
    answer_7_text = models.TextField(verbose_name="What would you like to name your autobiography?", max_length=1000)
    answer_8_text = models.TextField(verbose_name="You&apos;re a new addition to a crayon box. What color would you be and why?", max_length=1000)
    answer_9_text = models.TextField(verbose_name="What makes you believe that you are special?", max_length=1000)

    def __str__(self):
        return self.name

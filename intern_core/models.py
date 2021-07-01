from django import forms
from django.contrib.auth.models import User
from django.db import models



class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Company_Profile(User_Profile):
    image = models.ImageField(upload_to='company_image', null=True, blank=True, default='company_image/default.png')
    company_name = models.CharField(max_length=100)
    tax_id = models.IntegerField()
    foundation_year = models.IntegerField()


    def get_profile_url(self):
        return "/company_profile/{}".format(self.user.pk)


class Intern_Profile(User_Profile):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    department = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='intern_image', null=True, blank=True,
                              default='photos/id-card.png')

    def get_profile_url(self):
        return "/intern_profile/{}".format(self.user.pk)

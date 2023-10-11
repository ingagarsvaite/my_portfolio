
from django.db import models


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = "Contact_profiles"
        verbose_name = "Contact Profile"
        ordering = ["timestamp"]
    timestamp = models.DateField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    subject = models.CharField(verbose_name="Subject", max_length=100)
    message = models.TextField(verbose_name="Message", max_length=1000)

    def __str__(self):
        return f"{self.name}"


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = "Certificates"
        verbose_name = "Certificate"

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    title = models.CharField(blank=True, null=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CV(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    cv_file = models.FileField(upload_to="ingosapp/static/cv")


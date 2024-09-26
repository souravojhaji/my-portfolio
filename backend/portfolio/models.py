from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(default='http://default-url.com')  # Provide a default value here

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github = models.URLField()

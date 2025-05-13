from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student','STUDENT'),
        ('lecturer','LECTURER'),
        ('registrar','REGISTRAR'),
    ]

    role = models.CharField(max_length=10, choices= ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Issue(models.Model):
    STATUS_CHOICES= [
        ('open','OPEN'),
        ('assigned','ASSIGNED'),
        ('in_progress','IN_PROGRESS'),
        ('resolved','RESOLVED'),
    ]

    CATEGORY_CHOICES = [
        ('course','COURSE ISSUE'),
        ('exam','EXAM ISSUE'),
        ('registration','REGISTRATION ISSUE'),
        ('other','OTHER'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Issue_submitted')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='Issue_assigned', null=True, blank=True)
    category = models.CharField(max_length=20, choices = CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title






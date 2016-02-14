from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Member(AbstractBaseUser):
    """
    Custom user class.
    """
    username = models.CharField(max_length=30,unique=True,)
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

class Team(models.Model):
    team_name = models.CharField(max_length = 20)
    username = models.ManyToManyField(Member)
    
    def __str__(self):
        return self.team_name
    
class File(models.Model):
    file_name = models.CharField(max_length = 100)
    file_size = models.IntegerField(default = 0)
    file_data = models.CharField(max_length = 30)
    team_id = models.ForeignKey(Team)
    member_id = models.ForeignKey(Member)
    
    def __str__(self):
        return self.file_name
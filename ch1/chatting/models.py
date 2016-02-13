from __future__ import unicode_literals

from django.db import models

class Membership(models.Model):
    mem_username = models.CharField(max_length = 10)
    mem_mail = models.EmailField(max_length =70)
    mem_pass = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.mem_username
    
class Team(models.Model):
    team_name = models.CharField(max_length = 20)
    mem_username = models.ManyToManyField(Membership)
    
    def __str__(self):
        return self.team_name
    
class File(models.Model):
    file_name = models.CharField(max_length = 100)
    file_size = models.IntegerField(default = 0)
    file_data = models.CharField(max_length = 30)
    team_id = models.ForeignKey(Team)
    membership_id = models.ForeignKey(Membership)
    
    def __str__(self):
        return self.file_name
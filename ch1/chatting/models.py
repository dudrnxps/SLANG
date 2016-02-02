from __future__ import unicode_literals

from django.db import models

class Member(models.Model):
    m_id = models.CharField(max_length = 10, unique = True)
    m_mail = models.EmailField
    m_pass = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.m_id
    
class Team(models.Model):
    t_name = models.CharField(max_length = 20, unique = true)
    m_id = models.ManyToManyField(Member)
    
    def __str__(self):
        return self.t_name
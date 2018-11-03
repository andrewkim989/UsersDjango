from __future__ import unicode_literals
from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')


class UserManager(models.Manager):

    def add_validate(self, postData):
        errors = {}
        a = User.objects.filter(email = postData['email'])
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        elif not name_regex.match(postData['first_name']):
            errors["first_name"] = "First name should contain only letters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        elif not name_regex.match(postData['last_name']):
            errors["last_name"] = "Last name should contain only letters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid e-mail address"
        elif a:
            errors["email"] = "The email already exists in our system"
                
        return errors
    
    def edit_validate(self, postData):  
        errors = {}

        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        elif not name_regex.match(postData['first_name']):
            errors["first_name"] = "First name should contain only letters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        elif not name_regex.match(postData['last_name']):
            errors["last_name"] = "Last name should contain only letters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid e-mail address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

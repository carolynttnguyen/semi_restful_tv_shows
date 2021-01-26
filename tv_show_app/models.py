from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):
    # def basic_validator(self, postData):
    #     errors = {}
    #     if len(postData['title']) < 2:
    #         errors['title']= "Title must have more than 2 characters"
    #     if len(postData['network']) < 2:
    #         errors['network'] = 'Network needs to be at least 2 characters'
    #     if datetime.strptime(postData['release_date'],'%Y-%m-%d') > datetime.now():
    #         errors['release_date'] = 'Release Date should be in the past'
    #     if len(postData['description']) < 10:
    #         errors['description'] ='Description should be more than 10 characters'
    #     return errors

    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network field should be at least 3 characters'
        if postData['description'] != '' and len(postData['description']) < 10:
            errors['description'] = 'Description should be at least 10 characters'
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()

    def __repr__(self):
        return f'Show ID: {self.id} | Title: {self.title} | Network: {self.network} | Release Date: {self.release_date}| Description: {self.description}'
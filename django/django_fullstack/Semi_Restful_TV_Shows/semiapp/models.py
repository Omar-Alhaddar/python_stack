from django.db import models

class ShowManager(models.Manager):
    def create(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "description should be at least 10 characters"
        return errors

    def edit(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "description should be at least 10 characters"
        return errors

            

class Show(models.Model):
    title = models.CharField(max_length = 45)
    network = models.CharField(max_length = 45)
    reld = models.TextField(null=True)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
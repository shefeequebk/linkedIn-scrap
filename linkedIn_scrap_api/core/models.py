from django.db import models


class Post(models.Model):
    linkedIn_email = models.TextField()
    linkedIn_password = models.TextField()

    def __str__(self):
        return self.linkedIn_email

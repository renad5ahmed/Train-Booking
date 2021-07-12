from django.db import models

class User(models.Model):#hena de el database details
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    is_admin = models.BooleanField(default=False)
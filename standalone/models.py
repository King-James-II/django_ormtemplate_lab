from django.db import models  # Importing the models module from django.db for defining database models

# Test model
class Test(models.Model):
    name = models.CharField(max_length=30)  # Defining a CharField named 'name' with maximum length of 30 characters
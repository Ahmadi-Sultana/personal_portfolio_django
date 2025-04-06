from django.db import models

''' Create your models here. this is like a DAO Which will help us push the 
data into the database which will also tell the data types of the columns
we will be using postgres db
'''

class Job(models.Model):
    #image this will be stored into project not in db bes postgres is a relational db
    image = models.ImageField(upload_to='images/')
    #summary
    summary = models.CharField(max_length=200)



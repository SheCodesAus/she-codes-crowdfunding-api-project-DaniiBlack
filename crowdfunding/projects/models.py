from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Project(models.Model):
    # what does a project need? add below (title, description, goal etc ) 
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True)
    # note for 'owner' later this will nbeed to be changed to a foreign key, because there will be problems (Questions to be asked here.) Foreign Key vs Primary Key
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    # adding this project field, adding a little extra info so when the serializer goes to find the id it will find the id of this object
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
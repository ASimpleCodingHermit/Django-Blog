from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)
# Create your models here.
class Post(models.Model):
    # Title field using charfield constraint with unique constraint
    title=models.CharField(max_length=255) #title = character field with a max length of 255
 
    # Author field populated using the users database
    author=models.ForeignKey(User, on_delete=models.CASCADE) 
 
    # date and time fields automatically populated with system time
    # updated_on=models.DateField(auto_now=True)
    # created_on=models.DateField()
  
    # Body field to store our post
    body=models.TextField()
  
    # Status of post
    status=models.IntegerField(choices=STATUS, default=0)
    
    # Meta for the category
    # class Meta:
    #     ordering=['created_on']
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
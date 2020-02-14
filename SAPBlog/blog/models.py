from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):

    # variables
    author = models.ForeignKey('auth.User') #create and link one user (super user)
    title = models.CharField(max=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True) #able to leave box blank or null 

    # methods

    def publish(self):
        # when you hit publish button, then you can get the actual time
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    # string representation of model
    def __str__(self):
        return self.title


class Comment(model.Model):
    post = models.ForeignKey('blog.Post',related_name='comments') #connected to Post class
    author = models.CharField(max=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # Methods

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
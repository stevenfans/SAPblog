from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    # variables
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #create and link one user (super user)
    title = models.CharField(max_length=200)
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
    
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
    
    # string representation of model
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments', on_delete=models.CASCADE) #connected to Post class
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # Methods

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')


    def __str__(self):
        return self.text
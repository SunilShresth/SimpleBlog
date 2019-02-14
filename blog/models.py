from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

class BlogAuthor(models.Model):
    "Model representing author of a blog"
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Update your bio here.")

    class Meta:
        ordering = ['name', 'bio']

    def get_absolute_url(self):
        return reverse('blogs-by-author')

    def __str__(self):
        return self.name.username


class Blog(models.Model):
    "Model representing a blog post"
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(default=date.today)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class BlogComment(models.Model):
    "Model for representing comments of a blog post"
    description = models.TextField(max_length=1000, help_text="Enter your comment here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.description
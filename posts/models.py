from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # FIXED
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

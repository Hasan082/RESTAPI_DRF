from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Status(models.Model):
    """
    Model to represent the status of a User.
    """
    text = models.CharField(max_length=255, default="Status text")
    image_link = models.ImageField(upload_to='status_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]} - {'Private' if self.is_private else 'Public'}"
    
    class Meta:
        """
        Meta class to define ordering and verbose name.
        """
        ordering = ['-created_at']
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

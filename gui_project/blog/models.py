from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DailyLog(models.Model):
    CATEGORY_CHOICES = (
        ('FOOD', 'food'),
        ('MUSIC', 'music'),
        ('PROGRAMMING', 'programming'),
    )
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='PROGRAMMING')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author_id = User.pk
    content = models.TextField()
    main_image = models.ImageField()

    def __str__(self):
        return self.title


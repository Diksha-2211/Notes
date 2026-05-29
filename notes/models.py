from django.db import models
from django.contrib.auth.models import User

# for tags and colors
PASTEL_COLORS = [
    ('#FFE4E1', 'Pink'), 
    ('#E0FFFF', 'Light Cyan'), 
    ('#F5F5DC', 'Beige'),
    ('#E6E6FA', 'Lavender'),
    ('#F0FFF0', 'Honeydew'),
]

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # tag and color 
    tag = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=20, choices=PASTEL_COLORS, default='#FFE4E1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

import string, random
from django.db import models

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortURL(models.Model):
    url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True, default=generate_shortcode)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code

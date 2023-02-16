from django.db import models


class Item(models.Model):
    class Meta:
        ordering = ['uploaded_at']

    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    title = models.CharField(max_length=30, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    is_visible = models.BooleanField(default=True)

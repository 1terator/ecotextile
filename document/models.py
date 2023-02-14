from django.db import models


class Document(models.Model):
    class Meta:
        ordering = ['uploaded_at']

    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=200, blank=True, null=True)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.file.name

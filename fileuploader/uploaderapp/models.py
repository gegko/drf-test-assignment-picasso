from django.db import models


class File(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploaded_files')
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-uploaded_at']

from django.db import models

from django.contrib.auth.models import User
#from django.db import models
from django.core.exceptions import ValidationError

def validate_file(file):
    allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png', 'docx']
    ext = file.name.split('.')[-1].lower()

    if ext not in allowed_extensions:
        raise ValidationError("Only PDF, Image, and DOCX files are allowed")

    if file.size > 100 * 1024 * 1024:  # 10MB limit
        raise ValidationError("File too large (max 10MB)")

class Files(models.Model):
    name = models.CharField(max_length=255)
    files = models.FileField(upload_to='uploads/', null=True, blank=True)
    #files = models.FileField(upload_to='uploads/', validators=[validate_file])
    file_type = models.CharField(max_length=10, blank=True)
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #uploaded_at = models.DateTimeField(auto_now_add=True, default=None, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.file_type = self.files.name.split('.')[-1].lower()
        super().save(*args, **kwargs)

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name
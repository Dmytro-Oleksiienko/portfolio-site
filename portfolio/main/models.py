from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile_pics')
    role = models.CharField(max_length=50)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    location = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    cv_file = models.FileField(upload_to='cv_file', blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    tagline = models.CharField()
    gitlink = models.URLField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField()
    faculty = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    start_year = models.IntegerField(default=2022)
    end_year = models.IntegerField(default=2026)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'messages'
        managed = False  # Tells Django not to create this table, as FastAPI manages it
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

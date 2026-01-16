from django.db import models

# Create your models here.

class Estudent(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField(unique=True, blank=False, max_length=30)
    document = models.CharField(unique=True, blank=False, max_length=110)
    birth    = models.DateField()
    phone    = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Course(models.Model):
    NIVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    name        = models.CharField(max_length=100)
    description = models.TextField()
    duration    = models.IntegerField()
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    nivel       = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.name

class Course(models.Model):
    NIVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    name        = models.CharField(max_length=100)
    description = models.TextField()
    duration    = models.IntegerField()
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    nivel       = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    student     = models.ForeignKey(Estudent, on_delete=models.CASCADE, related_name="registrations")
    course      = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="registrations")
    created_at  = models.DateTimeField(auto_now_add=True)

    # Ensure a student can register for a course only once
    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} - {self.course}"
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField(default=25)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Extra fields for Phase 2 User Stories
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    organizer_name = models.CharField(max_length=100, default="TBD")

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    attendee_name = models.CharField(max_length=100)
    attendee_email = models.EmailField()
    comments = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee_name} - {self.event.title}"
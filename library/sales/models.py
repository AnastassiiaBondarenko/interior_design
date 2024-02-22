from django.db import models
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    phone_number = models.CharField(max_length=20, blank=False)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')

class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=200, blank=False)
    date_time = models.DateTimeField()
    SIZE_CHOICES = [
        ('small', 'Room only/small apartment'),
        ('medium', 'Medium apartment/house (2-3 rooms)'),
        ('big', 'Big apartment/house (4+ rooms)'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    DESIGN_CHOICES = [
        ('redesign', 'Redesign'),
        ('full_design', 'Full design from O'),
    ]
    design_type = models.CharField(max_length=20, choices=DESIGN_CHOICES)
    CONTACT_CHOICES = [
        ('phone', 'By phone'),
        ('email', 'By email'),
    ]
    contact_preference = models.CharField(max_length=10, choices=CONTACT_CHOICES)
    is_cancelled = models.BooleanField(default=False)

viktoriia = User.objects.create_user(username='viktoriia', email='192i912', password='21212')

admin_group = Group.objects.get(name='admin')
admin_group.user_set.add(viktoriia)

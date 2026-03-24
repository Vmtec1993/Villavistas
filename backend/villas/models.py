from django.db import models
from django.conf import settings

class Villa(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='villas/', default='villas/default.jpg')
    amenities = models.TextField(help_color="Comma separated: Pool, WiFi, Gym")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [('P', 'Pending'), ('C', 'Confirmed'), ('X', 'Cancelled')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Booking {self.id} - {self.villa.title}"

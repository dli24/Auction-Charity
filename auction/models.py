from django.db import models
from accounts.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Bid(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='bid')
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    start_amount = models.DecimalField(max_digits=12, decimal_places=2,validators=[MinValueValidator(0)])
    description = models.TextField(max_length=500)
    picture = models.TextField(null=True)

    def __str__(self):
        return self.name

class Bidding(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='bidding')
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='bidding')
    amount = models.DecimalField(max_digits=12, decimal_places=2,validators=[MinValueValidator(0)], null=True)

    def __str__(self):
        return str(self.amount)

class Comments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment')
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MaxValueValidator(9),MinValueValidator(0)])

    def __str__(self):
        return self.body

class Donation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='donation')
    donation_amount = models.DecimalField(max_digits=12, decimal_places=2,validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.donation_amount)
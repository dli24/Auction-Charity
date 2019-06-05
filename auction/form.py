from django import forms
from .models import Bid, Comments, Donation, Bidding

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('name','description','picture','start_date','end_date', 'start_amount')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body','rating')

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('donation_amount',)

class BiddingForm(forms.ModelForm):
    class Meta:
        model = Bidding
        fields = ('amount',)
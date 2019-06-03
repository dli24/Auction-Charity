from django.shortcuts import render, redirect
from .models import Bid, Comments, Donation
from django.contrib.auth.decorators import login_required
from .form import BidForm, CommentForm
from django.db.models import Sum
from django.contrib.auth.models import User
from accounts.models import Profile
from decimal import *

def landing(request):
	donations = Donation.objects.all().aggregate(Sum('donation_amount')).get('donation_amount__sum',0.00)
	bids = Bid.objects.all().aggregate(Sum('start_amount')).get('start_amount__sum', 0.00)
	bids= bids*Decimal(.15)
	total_donations = bids + donations
	return render(request, 'auction/landing.html', {'total_donations':total_donations})

def landing2(request):
	bids = Bid.objects.all()
	return render(request, 'auction/landing2.html')

def donation_form(request):
	return render(request, 'auction/donation_form.html')

def create_bid(request):
	if request.method == 'POST':
		name = request.POST['name']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		start_amount = request.POST['start_amount']
		description = request.POST['description']
		picture = request.POST['picture']
		user = request.user
		profile = Profile.objects.get(user=user.id)

		bid = Bid.objects.create(name=name, start_date=start_date, end_date=end_date, profile=profile, start_amount=start_amount, description=description, picture=picture)
		bid.save()
		return redirect('landing2')
	else:
		return render(request, 'auction/bid_form.html')
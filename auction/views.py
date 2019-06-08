from django.shortcuts import render, redirect
from .models import Bid, Comments, Donation, Bidding
from django.contrib.auth.decorators import login_required
from .form import BidForm, CommentForm, DonationForm, BiddingForm
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.models import User
from accounts.models import Profile
from decimal import *
from django.utils import timezone

def landing(request):
	donations = Donation.objects.all().aggregate(Sum('donation_amount')).get('donation_amount__sum',0.00)
	return render(request, 'auction/landing.html', {'donations':donations})

@login_required
def landing2(request):
	bids = Bid.objects.all().order_by('end_date')
	return render(request, 'auction/landing2.html', {'bids':bids})

@login_required
def donation_new(request):
	user = request.user
	profile = Profile.objects.get(user=user.pk)
	if request.method == 'POST':
		form = DonationForm(request.POST)
		if form.is_valid():
			donation = form.save(commit=False)
			donation.profile = profile
			donation.save()
			messages.success(request, 'Thank You for donating, God Bless You. PLEASE DONATE MORE! THANKYOU!')
			return redirect('donation_new')
	else:
		form = DonationForm()
	return render(request, 'auction/donation_form.html', {'form':form, 'profile': profile})

@login_required
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

@login_required
def bid_detail(request, bid_id):
	bid = Bid.objects.get(id=bid_id)
	user = request.user
	profile = Profile.objects.get(user=user.pk)
	bidding = Bidding.objects.filter(bid=bid.id).order_by('-amount').first()

	if bidding == None:
		current_bid = bid.start_amount
	else:
		current_bid = bidding.amount	
	if request.method == 'POST':
		form = BiddingForm(request.POST)
		if form.is_valid():
			new_bid = form.save(commit=False)
			new_bid.profile = profile
			new_bid.bid = bid
		if (new_bid.amount <= current_bid):
			return render(request, 'auction/bid_detail.html', {'bid':bid, 'error': 'Please enter an number that is greater than the current value.'})
		else:
			new_bid.bid = bid
			new_bid.save()
			return render(request, 'auction/bid_detail.html', {'bid':bid, 'current_bid': new_bid.amount})
	else:
		form = BiddingForm()
		return render(request, 'auction/bid_detail.html', {'bid':bid, 'profile':profile, 'current_bid':current_bid})

@login_required
def endbid(request):
	bids = Bid.objects.all()
	user = request.user
	profile = Profile.objects.get(user=user.pk)
	bidding = Bidding.objects.all().select_related('profile').select_related('bid').order_by('-amount').first()
	print(bidding)
	return render(request, 'auction/endbid.html', {'bids':bids, 'user':user, 'profile':profile, 'bidding':bidding})

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from .forms import ProfileForm
from .models import Profile
from auction.models import Bid, Comments, Donation

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error': 'That username has already been registered. Please try a different username'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {'error': 'That email has already been registered'})
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    user.save()
                    if user is not None:
                        auth.login(request, user)
                        return redirect('profile_create')
        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('landing2')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid Credentials...'})

    else:
        return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('landing')

@login_required
def profile_create(request):
    if request.method == 'POST':
        bio = request.POST['bio']
        picture = request.POST['picture']
        creditcard = request.POST['creditcard']
        user = request.user
        profile = Profile.objects.create(bio=bio, picture=picture, creditcard=creditcard, user=user)
        profile.save()
        return redirect('landing2')
    else:
        return render(request, 'accounts/profile_form.html')


@login_required
def profile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = request.user
    bids = Bid.objects.filter(profile=profile.pk)
    comments = Comments.objects.filter(profile=profile.pk)
    donations = Donation.objects.filter(profile=profile.pk)
    return render(request, 'accounts/profile.html', {'profile': profile, 'bids':bids, 'comments': comments, 'donations': donations, 'user': user})

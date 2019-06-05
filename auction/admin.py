from django.contrib import admin

from .models import Bid, Comments, Donation, Bidding

admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(Donation)
admin.site.register(Bidding)
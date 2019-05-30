from django.contrib import admin

from .models import Bid, Comments, Donation

admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(Donation)
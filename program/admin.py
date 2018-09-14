from django.contrib import admin
from .models import Profile, Week, Day, Exercise

admin.site.register(Profile)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Exercise)
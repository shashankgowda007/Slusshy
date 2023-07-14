from django.contrib import admin

# Register your models here.
from .models import Rate, Signup, Rider, Passenger, MAP, MapVal


admin.site.register(Rate)
admin.site.register(Signup)
admin.site.register(Rider)
admin.site.register(Passenger)
admin.site.register(MAP)
admin.site.register(MapVal)

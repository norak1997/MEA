from django.contrib import admin
from .models import *
# Questions,Placement,Events,Projects,Resources
# Register your models here.

admin.site.register(Questions)
admin.site.register(Placement)
admin.site.register(Events)
admin.site.register(Projects)
admin.site.register(Resources)


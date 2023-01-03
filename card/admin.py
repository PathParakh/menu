from django.contrib import admin

from .models import dish
from .models import owner
from .models import group

admin.site.register(dish)
admin.site.register(owner)
admin.site.register(group)
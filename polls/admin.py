from django.contrib import admin

# tell the admin that Question objects have an admin interface:
from .models import Question 

admin.site.register(Question)



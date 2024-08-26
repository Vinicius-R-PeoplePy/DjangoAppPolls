from django.contrib import admin
from django.urls import include, path
"""
When to use include()

You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
"""

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]

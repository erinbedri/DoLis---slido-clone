from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('DoLis.core.urls', 'DoLis.core.urls'), namespace='core')),
]

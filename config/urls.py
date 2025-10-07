from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app4/', include('app4.urls')),
    path('app5/', include('app5.urls')),
    path('app6/', include('app6.urls')),
]

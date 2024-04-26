from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path('', include('accounts.urls'))
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

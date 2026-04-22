

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from multi_shop import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("home.urls"))
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
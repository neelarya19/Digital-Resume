from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace="core")),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


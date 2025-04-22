from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('utilisateurs.urls')), 
    path('', include('ressources.urls')),
    path('', include('discussions.urls')),

]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

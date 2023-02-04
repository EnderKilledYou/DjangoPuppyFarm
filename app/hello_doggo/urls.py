from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from app.strings import views
from app.strings.views import HomeView

router = routers.DefaultRouter()
#router.register(r'users', views.PetViewSet)


urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('api/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

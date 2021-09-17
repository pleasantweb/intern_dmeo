from django.contrib import admin
from django.urls import path
from django.urls.conf import include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from decouple import config
from enroll import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('key',views.KeyValueApi,basename='key')

urlpatterns = [
    path(config('SECRET_ADMIN_URL') + '/admin/', admin.site.urls),
    path('api/',include(router.urls)),
]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name = 'index.html'))]
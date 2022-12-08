from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from fabric_api import router, settings

schema_view = get_schema_view(
   openapi.Info(
      title="Fabric API",
      default_version='v1',
      description="Автодокументация Fabric API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="https://t.me/namc0"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.router.urls)),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("api/__debug__/", include(debug_toolbar.urls)),)
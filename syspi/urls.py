"""
URL configuration for syspi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteListViewSet, PlanoListViewSet, FichaListViewSet, ContratoListViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema Pilates",
      default_version='v1',
      description="Documentação da API do projeto",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@meuprojeto.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'api/cliente', ClienteListViewSet, basename='cliente')
router.register(r'api/contrato', ContratoListViewSet, basename='contrato')
router.register(r'api/ficha', FichaListViewSet, basename='ficha')
router.register(r'api/plano', PlanoListViewSet, basename='plano')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("clientes.urls")),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

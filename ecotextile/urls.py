"""ecotextile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from user.views import MyObtainTokenPairView, RegisterView, UserViewSet
from document.views import DocumentViewSet
from item.views import ItemViewSet

router = routers.DefaultRouter()
router.register("documents", DocumentViewSet)
router.register("items", ItemViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path("v1/", include(router.urls)),
    path('v1/auth/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/auth/register/', RegisterView.as_view(), name='auth_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

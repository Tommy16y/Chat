"""chat URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from captcha.views import captcha_refresh


schema_view = get_schema_view(
    
    openapi.Info(
        title='Online chat',
        default_version='v1',
        description='chat',
    ),
    public = True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/',include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
    path('captcha/refresh/', captcha_refresh, name='captcha-refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

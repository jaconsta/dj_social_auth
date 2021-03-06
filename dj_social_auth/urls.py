"""dj_social_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from login_manager.views import register_by_access_token

urlpatterns = [
    # Templates.
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^views/login.html', TemplateView.as_view(template_name='login.html'), name="loginhtml"),
    # Config and admin.
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),

    # API endpoints
    url(r'^login/(?P<backend>[^/]+)', register_by_access_token),
]

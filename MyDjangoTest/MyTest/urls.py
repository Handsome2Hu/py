"""MyTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from MyTestApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^',include('MyTestApp.urls')),
    #url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    #url(r'^1',views.add2,name='add2'),
    #url(r'^qrcode',views.generate_qrcode,name='qrcode'),
    #url(r'^2',views.add3,name='add3'),

]

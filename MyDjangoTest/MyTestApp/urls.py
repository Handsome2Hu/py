from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'&',views.index),
    url(r'^1',views.add2,name='add2'),
    url(r'^qrcode',views.generate_qrcode,name='qrcode'),
    url(r'^2',views.add3,name='add3'),
]

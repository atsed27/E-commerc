
from django.urls import path,re_path
from .views import Products,ProductPart
from django.views.decorators.csrf import csrf_exempt
from middleware.verifayToken import VerifyToken

urlpatterns = [
    path('create',csrf_exempt(VerifyToken(Products.as_view()))),
    path('getAll',Products.as_view(),name='query'),
    re_path(r'^get/(?P<pk>[0-9a-f-]+)',ProductPart.as_view()),
    re_path(r'^update/(?P<pk>[0-9a-f-]+)',csrf_exempt(VerifyToken(Products.as_view()))),
    re_path(r'^delete/(?P<pk>[0-9a-f-]+)',csrf_exempt(VerifyToken(Products.as_view()))),
    

]
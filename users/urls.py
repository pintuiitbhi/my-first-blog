#users/urls.py

from django.conf.urls import url

from . import views

urlpatterns=[
url(r'signup/$',views.SignUp.as_view(),name='signup'),#class url
]
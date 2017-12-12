
from django.conf.urls import include, url

urlpatterns = [
url(r'^order/', include('cart.urls')),
]

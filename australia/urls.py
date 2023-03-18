from django.urls import path

from australia.views import *

app_name='australia'

urlpatterns=[
    path('smith/',smith,name='smith'),
    path('warner/',warner,name='warner'),
]
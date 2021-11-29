from django.urls import path
from . import views
urlpatterns=[
    path('log_app/',views.logfn,name='log_app'),
   
] 
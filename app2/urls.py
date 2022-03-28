from django.urls import path
from app2.views import app2_specific
app_name='app2'
urlpatterns=[path('app2_specific/',app2_specific,name='app2_specific'),]

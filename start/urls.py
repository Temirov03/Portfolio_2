from django.urls import path
from start.views import index


urlpatterns = [
    path("",index)
]
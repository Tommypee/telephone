from django.urls import path
from directory.views import *

urlpatterns = [
    path('', index ,name='index'),
    path('insert', insert ,name='insert'),
    path('remove/<int:id>/', remove ,name='remove'),
    path('amend/<int:id>/', amend ,name='amend'),
]

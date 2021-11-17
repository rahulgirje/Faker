from os import name
from django.urls import path
from .views import Homeview, Paginationshowview, Populate



urlpatterns=[
    path('',Homeview,name='home'),
    path('pol/',Populate,name='populate'),
    path('pagination/',Paginationshowview,name='pagination')
]
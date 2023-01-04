from django.urls import path
from  . import views

urlpatterns = [
    path('',views.home,name='home'),#Calling for home Page
    path('cameras',views.camera,name='cameras'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('overview',views.overview,name='overview'),
    path('analysis',views.analysis,name='analysis'),
    path('report',views.report,name='analysis'),
]

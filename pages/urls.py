from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('happysnapper',views.happysnapper,name="happysnapper"),
    path('tagnwin',views.tagnwin,name="tagnwin"),
    path('papertechrix',views.papertechrix,name="papertechrix"),
    path('register',views.register,name="register"),
    path('mindopedias',views.mindopedias,name="mindopedias"),
    path('blackbox',views.blackbox,name="blackbox"),
    path('retrofitzz',views.retrofitzz,name="retrofitzz"),
    path('projectcorner',views.projectcorner,name="projectcorner"),
    path('warriorsunite',views.warriorsunite,name="warriorsunite"),
    path('miraclebombshell',views.miraclebombshell,name="miraclebombshell"),
    path('funtasktik',views.funtasktik,name="funtasktik"),
    path('triathlon',views.triathlon,name="triathlon"),
    path('workshop',views.workshop,name="workshop"),
    path('offers',views.offers,name="offers")
]
from django.urls import path

from . import views
import blog.views as blog_views
urlpatterns = [
    path('about/', views.about, name='quesdb-about'),
    path('select/', views.select, name='quesdb-select'),
    path('tiankong/', views.tiankong, name='quesdb-tiankong'),
    path('failtofind/', views.failtofind, name='quesdb-failtofind'),
    path('add/', views.add, name='quesdb-add'),
    path('tkadd/', views.tkadd, name='quesdb-tkadd'),
    path('success/', views.success, name='quesdb-success'),
    path('answer/', views.answer, name='quesdb-answer'),
    path('searchfortest/', views.searchfortest, name='quesdb-searchfortest'),
    path('givescore/', views.givescore, name='quesdb-givescore'),
    path('makejudge/', views.makejudge, name='quesdb-makejudge'),
    path('updatedb/', views.updatedb, name='quesdb-updatedb'),
    path('tkupdatedb/', views.tkupdatedb, name='quesdb-tkupdatedb'),
    path('first/', views.first, name='quesdb-first'),
    path('newTorS/', views.newTorS, name='quesdb-newTorS'),
    path('addTorS/', views.addTorS, name='quesdb-addTorS'),
    path('otherscore/', views.otherscore, name='quesdb-otherscore'),
    path('myscore/', views.myscore, name='quesdb-myscore'),
    path('excellentscore/', views.excellentscore,name='quesdb-excellentscore'),
    path('', views.home, name='home'),
]

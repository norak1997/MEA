from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('placements', views.placements, name='Placements'),
    path('tests', views.tests, name='Tests'),
    path('events', views.events, name='Events'),
    path('projects',views.projects, name='Projects'),
    path('projects/<name1>',views.specprojects, name='Projects1'),
    path('events/<name1>',views.specevents, name='Events1'),
    path('placements/<name1>/<comp>',views.specplacements, name='Placements1'),
    path('tests/<cat>',views.spectests, name='Tests1'),
    path('check',views.check, name='Tests1'),
]
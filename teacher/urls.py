from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as teacher_views
urlpatterns =[

	url(r'^$', teacher_views.index, name ='index'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', teacher_views.signup, name='signup'),
	url(r'^(?P<teacher_username>[0-9]+)/$', teacher_views.detail , name = 'detail' ),
]
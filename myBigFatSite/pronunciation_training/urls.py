from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html')),		
	#url(r'^$', views.index, name='pronunciation_training'),
]


# Copy from dev_blog

# url(r'^$', views.index, name='blog'),


# The following was changed to above to make homepage pronunciation training
"""
from django.conf.urls import url
from django.views.generic import TemplateView

# from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html')),
]
"""

"""myBigFatSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mybigfathomepage import views
from dev_blog import urls	#views
from dev_blog import urls	#views
#from dev_blog import views
#from pronunciation_training import views
# For homeview


# Idea for Homepage :: then add to Templates/index.html
from django.views.generic import TemplateView


"""
From static sites:
urlpatterns = patterns('',
	url(r'^pronunciation_training/', include('pronunciation_training.urls')),
	url(r'^dev_blog/', include('dev_blog.urls')),
	url(r'^admin/', admin.site.urls),
)
"""
urlpatterns = [
	# Set up a homapage view rather that pron_tran http
	#url(r'^$', HomeView.as_view(), name='home'),
	#url(r'^$', views.index, name='blog'),
	#url(r'^$', views.index, name='index'),
	url(r'^$', views.index, name='index'),	# Should point to home_app
	url(r'^dev_blog/', include('dev_blog.urls')),	# Should point to /blog html
	url(r'^pronunciation_training/', include('pronunciation_training.urls')), #pron_trn html
    url(r'^admin/', admin.site.urls),	#points to /admin
]


"""
FROM MYSITE DEMO urls.py:

from django.conf.urls import include, url
from django.contrib import admin
from polls import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', admin.site.urls),
]

"""

from django.shortcuts import render
from django.utils import timezone
#from django.http import HttpResponse

def index(request):
	def	get(request):
		TemplateView.as_view(template_name='index.html')
"""

def index(request):
	return render(request, 'pronunciation_training/index.html')

"""








# from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.generic import TemplateView

# Create your views here.





# From urls, this change to make homepage pronunciation training html and not project homepage:

"""
from django.conf.urls import url
from django.views.generic import TemplateView

# from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html')),
]
"""

from django.shortcuts import render
from django.utils import timezone
from .models import BlogPost
#from django.http import HttpResponse

# Create your views here.


"""
def index(request):
	return HttpResponse("You are at James' dev_blog app!!")
"""

def index(request):
	posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'dev_blog/post_list.html', {'posts': posts})


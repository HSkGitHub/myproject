from django.shortcuts import render
from django.http import HttpResponse
# from yitaowang.models import Page, Subject

def index(request):
	context_init = {'boldmessage' : "static"}
	return render(request, 'subtemplate/index.html',context_init)

def about(request):
	return HttpResponse("this is about : <br/> <a href='/yitaowang/'>about<a>")
	


# Create your views here.

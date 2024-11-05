from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template



def members(request):
  template = get_template('index.html')
  return HttpResponse(template.render())
  #return render(request, 'index.html')
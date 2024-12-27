from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
def member(request):
    # template = loader.get_template('index.html')
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers' : mymembers,
    }

    return HttpResponse(template.render(context,request))
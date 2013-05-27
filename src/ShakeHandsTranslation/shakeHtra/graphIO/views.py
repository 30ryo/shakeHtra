from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from models import *
from django import forms
from django.template import Context,loader
from django.utils import simplejson

def index(request):
    form = TestForm()
    context = Context({"form":form})
    temp = loader.get_template('graphIO/index.html')
    return HttpResponse(temp.render(context))

class TestForm(forms.Form):
    test = forms.HiddenInput()

def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            content = simplejson.dumps({"result": "success"}) 
            return  HttpResponse(content, mimetype="text/javascript")
    raise Http404
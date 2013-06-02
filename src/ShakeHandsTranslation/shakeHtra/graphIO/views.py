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

def initialJson(request):
    
    nodes = [{"id": 10, "reflexive": False},
             {"id": 11, "reflexive": False},
             {"id": 12, "reflexive": False}]
    links = [{"source": nodes[0], "target": nodes[1], "left": False, "right": True},
             {"source": nodes[1], "target": nodes[2], "left": False, "right": True}]

    content = simplejson.dumps({"nodes":nodes,
                                "lastNodeId":12,
                                "links":links
                                }) 
    
    return HttpResponse(content, mimetype="application/json")
import json
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    # return HttpResponse("Hello, Django!")
    notebook = None
    try:
        notebook = json.loads(open(f"{os.path.dirname(__file__)}/sample.ipynb").read())
    except Exception as e:
        # logger.warning(e)
        exit(1)

    print(notebook)
    for c in notebook['cells']:
        print(c['cell_type'])
        print(c['source'])

    return TemplateResponse(request, "base.html", notebook)

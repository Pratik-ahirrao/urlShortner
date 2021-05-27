from django.shortcuts import render,redirect
import uuid
from .models import url
from django.http import HttpResponse


# Create your views here.

def index(req):
    return render(req, 'index.html')


def create(req):
    if req.method == 'POST':
        link = req.POST['link']
        uid = str(uuid.uuid4())[:5]  # unique id of length 5
        new_url = url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(req, pk):
    final_url = url.objects.get(uuid=pk)
    return redirect(final_url.link)

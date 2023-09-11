from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Url
import uuid


def index(req):
    return render(req, 'index.html')


def create(req):
    if req.method == 'POST':
        link = req.POST['link']
        uid = str(uuid.uuid4())[:5]

        new_url = Url(link=link, uuid=uid)
        new_url.save()

        return HttpResponse(uid)


"""
Redirect to a page based on pk(uuid)
"""
def go(req, pk):
    url_details = Url.objects.get(uuid=pk)

    return redirect('https://' + url_details.link)

import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.utils.encoding import smart_str

from .models import PrintRequest
from .forms import PrintRequestForm

def index(request):
    printlist = None
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login/')
    if request.method == 'POST':
        form = PrintRequestForm(request.POST, request.FILES)
        if form.is_valid():
            printreq = PrintRequest()
            printreq.username = request.user
            printreq.source = request.FILES['source']
            printreq.save()
            return HttpResponseRedirect('/')
    else:
        form = PrintRequestForm()
        if request.user.is_authenticated:
            printlist = PrintRequest.objects.filter(username=request.user).order_by('-req_time')
    return render(request, 'index.html', {
        'form': form,
        'printlist': printlist,
    })

def staff(request):
    if request.user.is_staff:
        if request.method == 'POST':
            printreq = PrintRequest.objects.get(pk=request.POST['file'])
            printreq.printed=not printreq.printed
            printreq.save()
            return HttpResponseRedirect('/staff/')
        else:
            printlist = PrintRequest.objects.order_by('-req_time')
            return render(request, 'staff.html', {
                'printlist': printlist,
            })
    else:
        raise Http404()

def source_view(request, username, filename):
    if request.user.username == username or request.user.is_staff:
        f = open(os.path.join(settings.BASE_DIR, 'files/source/' + username + '/' + filename), 'r')
        contents = f.read()
        f.close()
        return render(request, 'source.html', {
            'filename': filename,
            'username': username,
            'contents': contents,
            'print': False,
        })
    else:
        raise Http404()

def print_view(request, username, filename):
    if request.user.is_staff:
        f = open(os.path.join(settings.BASE_DIR, 'files/source/' + username + '/' + filename), 'r')
        contents = f.read()
        f.close()
        return render(request, 'source.html', {
            'filename': filename,
            'username': username,
            'contents': contents,
            'print': True,
        })
    else:
        raise Http404()

def handler404(request):
    return render(request, '404.html', status=404)
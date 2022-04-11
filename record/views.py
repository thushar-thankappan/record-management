from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import PersonnelForm
from .models import User
def add(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            form = PersonnelForm()
    else:
        form = PersonnelForm()
    info = User.objects.all()
    return render(request, 'record/createandretrive.html', {'form': form, 'info': info})


def delete_data(request, id):
    if request.method == 'POST':
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    user = User.objects.all()
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        form = PersonnelForm(request.POST, instance=up)
        if form.is_valid():
            form.save()
    else:
        up = User.objects.get(pk=id)
        form = PersonnelForm(instance=up)

        
    return render(request, 'record/update.html', {'id': id, 'user': user, 'form': form})


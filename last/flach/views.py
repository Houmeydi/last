from django.shortcuts import render,redirect, get_object_or_404
from .models import Livre, Auteur
from .forms import someforms

def index(request):
    return render(request, template_name='flach/index.html', context={'livres': Livre.objects.all()})

"""
def index(request):
    form=someforms(request.POST or None)
    if form.is_valid():
        redirect(" flach:index ")
    else:
        form=someforms()
    return render(request, template_name='flach/index.html',context={'form':form })
"""

def show(request, livre_id):
    return render(request, template_name='flach/show.html', context={'livre': get_object_or_404(Livre,pk=livre_id)})

def add(request):
    if request.method=='POST':
         form=someforms(request.POST or None)
         if form.is_valid():
            form.save()
            return redirect("flach:index")
    else:
        form=someforms()
    return render(request, template_name='flach/livre_forms.html',context={'form':form })

    
def delete(request, livre_id):
    livre=Livre.objects.get(pk=livre_id)
    livre.delete()
    return redirect("flach:index")

def modifie(request,livre_id):
    livre=Livre.objects.get(pk=livre_id)
    if request.method=='POST':
         form=someforms(request.POST or None, instance=livre)
         if form.is_valid():
            form.save()
            return redirect("flach:index")
    else:
        form=someforms()
    return render(request, template_name='flach/livre_forms.html',context={'form':form })
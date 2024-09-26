from django.shortcuts import render, redirect
from .models import Diaries
from .forms import DiariesForm

# Create your views here.

def index(request):
    diary = Diaries.objects.all()
    context = {
        'diary' : diary,
    }
    
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = DiariesForm(request.POST)
        if form.is_valid():
            diary = form.save()
            return redirect('diaries:index')
    else: form = DiariesForm()
    
    context = {
        'form': form,
    }
    
    return render(request,'create.html', context)
 
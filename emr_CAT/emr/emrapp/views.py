from django.shortcuts import render, redirect
from .forms import RecordForm
from .models import *

# Create your views here.
def indexform(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/dash')
    context = {'form': form}
    return render(request, 'index.html', context)

def dash(request):
    obj = records.objects.all()
    return render(request, 'dash.html', {'obj':obj})
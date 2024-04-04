from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def avatarView(request):
  
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'myapp/studentform.html', {'form' : form})
  
  
def uploadok(request):
    return HttpResponse(' upload successful')
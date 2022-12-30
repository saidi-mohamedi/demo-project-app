from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .form import ProjectForm 
from .models import Project


def dashboard(request):
    project = Project.objects.all()
    context = {'project':project }
    return render(request, 'demoApp/dashboard.html', context)  
    
def index(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project':project} 
    return render(request, 'demoApp/index.html',context) 

def createProject(request):
    form = ProjectForm() 
    if  request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'demoApp/project_form.html', context)  



def updateProject(request,pk):
    updateproject = Project.objects.get(id=pk)
    form = ProjectForm(instance=updateproject) 
    if  request.method == 'POST':
        form = ProjectForm(request.POST,instance=updateproject)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'demoApp/project_form.html', context)  


def deleteProject(request,pk):
    deleteproject = Project.objects.get(id=pk)
    if  request.method == 'POST':
        deleteproject.delete()
        return redirect('dashboard')
    context = {'deleteproject':deleteproject}
    return render(request, 'demoApp/delete.html', context)  

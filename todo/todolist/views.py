from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from todolist.forms import RegistrationForm
from todolist.models import List,Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    if request.user.id==None:
        return render(request,'welcome.html')
    else:
        current_user=User.objects.get(username=request.user.username)
        lists=current_user.list_set.all()
        tasks=[]
        for i in lists:
            tasks.append(i.task_set.all())
        tasksNlists=zip(tasks,lists)
        if 'addList' in request.POST:
            listname=request.POST['listname']
            current_user.list_set.create(name=listname)
        if 'addTask' in request.POST:
            taskname=request.POST['taskname']
            list_no=request.POST['listid']
            current_list=List.objects.get(id=list_no)
            current_list.task_set.create(name=taskname)
        if 'close' in request.POST:
            print(request.POST)
            for Ltasks in tasks:
                for t in Ltasks:
                    status=request.POST.get('cstat'+str(t.id))
                    if status=='on':
                        t.completed=True
                        status=None
                    elif(status==None):
                        t.completed=False

        return render(request, 'home.html', {'id': request.user.id, 'username': request.user.username, 'lists':lists, 'tasksNlists':tasksNlists})

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            passwrd = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=passwrd)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def loginuser(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            passwrd = form.cleaned_data.get('password')
            user = authenticate(username=user, password=passwrd)
            login(request, user)   
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logoutuser(request):
    logout(request)
    return redirect('home')

def task_view(request, list_id):
    current_list=List.objects.get(pk=list_id)
    data=current_list.task_set.all()
    return render(request, 'tasks.html', {'tasks': data})
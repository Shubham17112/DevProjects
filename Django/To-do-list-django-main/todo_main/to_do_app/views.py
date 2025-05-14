from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404, redirect
from to_do_app.models import todo
from django.contrib.auth.decorators import login_required




def index(request):
    if request.user.is_authenticated:
        user = request.user
        todos = todo.objects.filter(user = request.user)
        for i, task in enumerate(todos, start=1):
            task.display_number = i
        return render(request, 'to_do_app/index.html', {'todos': todos,'user':user})
    
    return redirect('to_do_auth:singup')
@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_task = todo(title=title,user = request.user)
        new_task.save()
    return redirect('to_do:index')
@login_required
def delete (request,id):
    todo.objects.get(id=id,user = request.user).delete()
    return redirect('to_do:index')
@login_required
def update (request,id):
    to_do_object = get_object_or_404(todo, pk = id,user = request.user)
    if request.method == 'POST':
        if request.POST.get('isCompleted') == 'on':
            iscompleted =  request.POST.get('isCompleted')
            print(iscompleted)
            if iscompleted :    
                print('inside funtion iscomplete')
                to_do_object.isCompleted = True
        else:
             to_do_object.isCompleted = False
        if request.POST.get('title'):
            to_do_object.title = request.POST.get('title')

        to_do_object.save()
            
    return redirect('to_do:index')
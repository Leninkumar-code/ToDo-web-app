from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
from todo.forms import ToDoForm
from todo.models import ToDo

# ------------------------------for create and view---------------------->
def index (request):
    item_list = ToDo.objects.order_by("-date")
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('todo')
    form = ToDoForm()
    
    page = {
        'forms': form,
        'list': item_list,
        'title': 'ToDo List',
    }
    return render(request,'todo/index.html',page)

# ----------------------------for delete existing one--------------------->
def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item removed !!!")
    return redirect('todo')
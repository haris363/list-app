from django.shortcuts import render , redirect, get_object_or_404

# Create your views here.
from .models import Todo
from django.urls import path
from django.shortcuts import render , redirect

from django.views import View
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegisterViews(View):
    def get (self,request,*args, **kwargs):
        form = RegisterForm()
        return render(request,'register.html', {'form': form})
    def post (self,request,*args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
          user = form.save() 
          login(request,user)
          return redirect('dashboard')
          
class DashboardViews(LoginRequiredMixin,View):
      def get (self,request,*args, **kwargs):
      
        return render(request,'dashboard.html')

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        
      
        todo = Todo.objects.create(title=title)
        todo.save()
        return redirect('dashboard')
    return render(request, 'dashboard.html' )

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    
    return redirect('dashboard')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('dashboard')



def edit(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        # Directly updating the Todo item
        title = request.POST.get('title')  # Get new title from form data
        todo.title = title  # Update the title
        todo.save()  # Save the updated Todo item
        return redirect('dashboard')  # Redirect back to the Todo list page

    # If GET request, just display the edit page with current Todo details
    return render(request, 'dashboard.html', {'todo': todo})

def dashboard(request):
    todos = Todo.objects.all()
    return render(request, 'dashboard.html', {'todos': todos})

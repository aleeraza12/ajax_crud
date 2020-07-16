from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.views.generic import ListView
from .models import CrudUser,Product,Tasks
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
from django.contrib import messages
#from django.core.mail import send_email
from django.conf import settings
from .forms import *
from django.contrib.auth.models import User
from django.views.generic.edit import View
from django.http import JsonResponse


#We are getting the form data using request.GET.get(address, None),
#address is the form’s input name attribute. Then we are creating a user
# and sending back the user which we have created so to display it on the web page.

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud.html'
    context_object_name = 'users'



class ProductView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'



def index(request):
    tasks = Tasks.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form =  TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Saved Successfully')
            return redirect('/list')
    context = {'tasks':tasks,'form':form}
    return render(request,'crud_ajax/list.html',context)

def UpdateTask(request,pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form =  TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.info(request,'Data Updated Successfully')
        return redirect('list')
    context = {'form':form}
    return render(request,'crud_ajax/update_form.html',context)


def DeleteTask(request,pk):
    item = Tasks.objects.get(id=pk)
    if request.method == 'POST':
            item.delete()
            messages.error(request,'Data Deleted Successfully')
            return redirect('/list')
    context= {'item':item}
    return render(request,'crud_ajax/delete_form.html',context)

def loginPage(request):
    if request.user.is_authenticated:
            return redirect('list')
    else:
         if request.method == 'POST':
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request, username=username,password=password)
             if user is not None:
                    login(request , user)
                    return redirect('list')
             else:
                    messages.info(request,'User name or password is incorrect')
    return render(request, 'users_registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
     if request.user.is_authenticated:
          return redirect('list')
     else:
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request,'Account created successfully of ' + username)
                return redirect('login')
            context = {'form': form}
            return render(request, 'users_registration/ajax/register1.html', context)


class ValidateUsername(View):
    def get(self, request):
        email = request.GET.get('email', None)
        data = {
            'is_present': User.objects.filter(email__iexact=email).exists()
        }
        return JsonResponse(data)


def book_list(request):
    books = Books.objects.all()
    context = {'books':books}
    return render(request, 'upload_files/book_list.html',context)


def upload_book(request):
    if request.method == 'POST':
        bookform = BookForm(request.POST,request.FILES)
        if bookform.is_valid():
            bookform.save()
            return redirect('upload_book')
    else:
        bookform = BookForm()
        context = {'bookform':bookform}
        return render(request, 'upload_files/upload_book.html',context)

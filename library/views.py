from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import *
from.models import *

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect!'})

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            user_obj = User.objects.filter(username=request.POST['email'])
            print(user_obj,'+++++++++++++++++++++++++++++++++')
            if user_obj:
                return render(request, 'register.html', {'error':'Email is already taken'})
            
            else:
                user = User.objects.create_user(email = request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('login')

        else:
            return render(request, 'register.html', {'error':'Password doesn\'t matched'})

    else:
        return render(request, 'register.html')

def logout(request):
    logout(request)
    return redirect('login')

#from django.contrib.sessions.models import Session

def home(request):
    #if request.session.has_key('is_logged'):
        book_obj = Book.objects.all().order_by("-id")
        contaxt = {
        "book_obj":book_obj
    }
        return render(request,'home.html',contaxt)
    #return redirect('login')

def update(request,id):
    book_obj = Book.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        print(name)
        print(price)
        print(description)
        print(image)

        book_data = Book.objects.filter(id = id).update(
            book_name = name,
            price = price , 
            description = description,
            image = image
        )
        return redirect("/")

    contaxt = {
        "book_obj":book_obj
    }
    return render(request,'update.html',contaxt)

def delete_book(request,id):
    Book.objects.get(id = id).delete()
    return redirect("/")

def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        print(name)
        print(price)
        print(description)
        print(image)

        book_data = Book.objects.create(
            book_name = name,
            price = price , 
            description = description,
            image = image
        )
        return redirect("/")
    return render(request,'add.html')
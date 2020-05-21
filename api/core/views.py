from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book
from .forms import BookForm


@login_required(login_url='/login')
def create_book(request):
    if request.POST:
        city = request.POST.get('city')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        user = request.user
        photo = request.FILES.get('photo')
        book = Book.objects.create(
        city=city, description=description, phone=phone, email=email, user=user, photo=photo)
        return redirect('/')
    return render(request, 'create-book.html')


def read_book(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


@login_required(login_url='/login')
def update_book(request, id):
    if request.POST:
        book = Book.objects.get(id = id)
        book.email = request.POST.get('email')
        book.phone = request.POST.get('phone')
        book.city = request.POST.get('city')
        book.description = request.POST.get('description')
        photo = request.FILES.get('photo')
        if photo:
            book.photo = photo
        book.save()
        return redirect('/')
    book = Book.objects.get(id = id)
    return render(request, 'book-update.html', {'book' : book})




@login_required(login_url='/login')
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')


def detail_book(request, id):
    book = Book.objects.get(id = id, user = request.user)
    print(book.id)
    return render(request, 'book-detail.html', {'book': book})


@csrf_protect
def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return render(request, 'login.html')


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/')


@csrf_protect
def create_user(request):
    if request.POST:
        username = request.POST.get('username_register')
        password = request.POST.get('password_register')
        user = User.objects.create(username = username, password = password, is_staff = 1)
        return redirect('/login')
    return render(request, 'register-user.html')

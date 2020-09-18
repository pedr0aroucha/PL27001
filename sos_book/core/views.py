from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Book, Ebook

# Book Views
###############################################################


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


@login_required(login_url='/login')
def read_book(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})


@login_required(login_url='/login')
def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.POST:
        book.email = request.POST.get('email')
        book.phone = request.POST.get('phone')
        book.city = request.POST.get('city')
        book.description = request.POST.get('description')
        photo = request.FILES.get('photo')
        if photo:
            book.photo = photo
        book.save()
        return redirect('/book/read')
    return render(request, 'book-update.html', {'book': book})


@login_required(login_url='/login')
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/')

# Views Book +
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


@login_required(login_url='/login')
def detail_book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book-detail.html', {'book': book})

# Ebook views
###############################################################


@login_required(login_url='/login')
def create_ebook(request):
    if request.POST:
        description = request.POST.get('description')
        user = request.user
        photo = request.FILES.get('photo')
        file = request.FILES.get('file')
        book = Ebook.objects.create(
            description=description, user=user, photo=photo, ebook=file)
        return redirect('/')
    return render(request, 'create-ebook.html')


@login_required(login_url='/login')
def read_ebook(request):
    ebooks = Ebook.objects.all()
    return render(request, 'list-ebook.html', {'ebooks': ebooks})


@login_required(login_url='/login')
def update_ebook(request, id):
    ebook = Ebook.objects.get(id=id)
    if request.POST:
        ebook.description = request.POST.get('description')
        photo = request.FILES.get('photo')
        if photo:
            book.photo = photo
        file = request.FILES.get('file')
        ebook.save()
        return redirect('/ebook/read')
    return render(request, 'ebook-update.html', {'ebook': ebook})


@login_required(login_url='/login')
def delete_ebook(request, id):
    ebook = Ebook.objects.get(id=id)
    ebook.delete()
    return redirect('/')

# Views Ebook +
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


@login_required(login_url='/login')
def detail_ebook(request, id):
    ebook = Ebook.objects.get(id=id)
    return render(request, 'ebook-detail.html', {'ebook': ebook})

# views for all
###############################################################


@login_required(login_url='/login')
def my_book(request):
    books = Book.objects.filter(user=request.user)
    ebooks = Ebook.objects.filter(user=request.user)
    return render(request, 'my.html', {'books': books, 'ebooks': ebooks})


@csrf_protect
def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
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
    return redirect('/login')


@csrf_protect
def create_user(request):
    form = UserCreationForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(
                request, "O Usuário/Senha que você digitou não atendem as requisito")
    return render(request, 'register-user.html', {'form': form})


def dev(request):
    return render(request, 'dev.html')

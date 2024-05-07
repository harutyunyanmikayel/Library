from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Client, Book, Author, Reservation
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


def client_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'books/register.html', {'error_message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'books/register.html', {'error_message': 'Username is already taken'})
        if User.objects.filter(email=email).exists():
            return render(request, 'books/register.html', {'error_message': 'Email is already registered'})

        user = User.objects.create_user(first_name=name, last_name=surname, username=username, email=email,
                                        password=password1)
        user.save()

        client = Client.objects.create(user=user, address=address)
        client.save()

        email_sender(user)

        return redirect('login')
    else:
        return render(request, 'books/register.html')


def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'books/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'books/login.html')


def client_logout(request):
    logout(request)
    return redirect('home_page')


def home_page(request):
    authors = Author.objects.all()

    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query)

    elif query == '':
        return redirect(reverse('home_page'))

    else:
        books = []

    return render(request, 'books/home.html', {'authors': authors, 'books': books, 'query': query})


def feedbacks_page(request):
    return render(request, 'books/feedbacks.html')


def contact_page(request):
    return render(request, 'books/contact.html')


def author_page(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)

    return render(request, 'books/author.html', {'books': books, 'author': author})


def book_page(request, author_id, book_title):
    book = get_object_or_404(Book, title=book_title)

    reservation = None

    if request.method == 'POST':
        client = get_object_or_404(Client, user=request.user)
        if book.is_available:
            reservation = Reservation.objects.create(book=book, client=client,
                                                     expiration_date=timezone.now() + timezone.timedelta(days=30))
            reservation.save()
            book.is_available = False
            book.save()

        elif 'cancel' in request.POST:
            reservation = Reservation.objects.get(book=book)
            reservation.delete()

        return redirect('home_page')

    else:
        try:
            reservation = Reservation.objects.get(book=book)
        except Reservation.DoesNotExist:
            pass

    return render(request, 'books/book.html', {'book': book, 'author_id': author_id, 'reservation': reservation})


def email_sender(user):
    subject = "Congratulations!"
    message = "Welcome to our Library! Here you can find a lot of interesting books."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}')

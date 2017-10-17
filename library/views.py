from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Publisher
from datetime import datetime
# Create your views here.

def index(request):
    books = Book.objects.all()[:10]
    author = Author.objects.all()
    context = {
        'books': books,
        'author': author,
    }
    return render(request, 'library/home.html', context)


def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'library/books.html', context)

def author(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'library/authors.html', context)

def publisher(request):
    publishers = Publisher.objects.all()
    context = {
        'publishers': publishers
    }
    return render(request, 'library/publishers.html', context)


#Detail views
def author_details(request, author_id):
    authorDetails = get_object_or_404(Author, pk=author_id)
    context = {
        'authorDetails': authorDetails
    }
    return render(request, 'details/authorDetails.html', context)

def publisher_details(request, pub_id):
    publisherDetails = get_object_or_404(Publisher, pk=pub_id)
    context = {
        'publisherDetails': publisherDetails
    }
    return render(request, 'details/pubDetails.html', context)

#add an author
def add(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        email = request.POST['email']

        author = Author(author_name=name, author_address=address, birthday=birthday, phone_number=phone, author_email=email)
        author.save()

        return redirect('/home/author')
    else:
        return render(request, 'forms/add_author.html')

#modifying an author's details
def modify(request, author_id):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        email = request.POST['email']

        a = Author.objects.get(pk=author_id)
        

        a.author_name = name
        a.author_address = address
        a.birthday = birthday
        a.phone_number = phone
        a.author_email = email
        a.save()

        return redirect('/home/author')
    else:
        author = get_object_or_404(Author, pk=author_id)
        return render(request, 'forms/modify_author.html', {'author': author})

#adding a publisher
def addpub(request):
    if(request.method == 'POST'):
        p_name = request.POST['p_name']
        p_address = request.POST['p_address']
        p_email = request.POST['p_email']
        web = request.POST['web']

        publisher = Publisher(publisher_name=p_name, publisher_address=p_address, publisher_email=p_email, web=web)
        publisher.save()

        return redirect('/home/publisher')
    else:
        return render(request, 'forms/add_publisher.html')



def modify_pub(request, pub_id):
    if(request.method == 'POST'):
        p_name = request.POST['p_name']
        p_address = request.POST['p_address']
        p_email = request.POST['p_email']
        web = request.POST['web']

        p = Publisher.objects.get(pk=pub_id)
        p.publisher_name = p_name
        p.publisher_address = p_address
        p.publisher_email = p_email
        p.web = web
        p.save()

        return redirect('/home/publisher')
    else:
        publisher = get_object_or_404(Publisher, pk=pub_id)
        return render(request, 'forms/modify_publisher.html', {'publisher': publisher})


def addbook(request):
    if(request.method == 'POST'):
        b_title = request.POST['b_title']
        b_isbn = request.POST['b_isbn']
        b_year = request.POST['b_year']
        b_author = request.POST['b_author']
        b_publisher = request.POST['b_publisher']

        book = Book(title=b_title, isbn=b_isbn, year=b_year, author=b_author, publisher=b_publisher)
        book.save()
        
        return redirect('/home/books')
    else:
        author = Author.objects.all()
        publisher = Publisher.objects.all()
        books = Book.objects.all()
        context = {
            'author': author,
            'publisher': publisher,
            'books': books,
        }
        
        return render(request, 'forms/add_books.html', context)





#delete author, and publisher views

def delete_a(request, author_id):
    if(request.method == 'DELETE'):
        try:
            a = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return HttpResponse("Author does not exist")
        a.delete()
        return redirect('/home/author') 

def delete_p(request, pub_id):
    if(request.method == 'DELETE'):
        try:
            p = Publisher.objects.get(pk=pub_id)
        except Publisher.DoesNotExist:
            return HttpResponse("Publisher does not exist")
        p.delete()
        return redirect('/home/publisher') 
        
    


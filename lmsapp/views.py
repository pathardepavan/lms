from django.views import generic
from .models import Publisher,Author,Book,Issue
from .forms import PublisherCreateForm,AuthorCreateForm,BookCreateForm,IssueCreateForm,LoginForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from datetime import datetime,timedelta
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# class HomePage(generic.TemplateView):
#     template_name = "home.html"

def home(request):
    return render(request,'lmsapp/home.html')

class AboutPage(generic.TemplateView):
    template_name = "about.html"

def logout_user(request):
    if request.user.is_active:
        logout(request)
        return HttpResponseRedirect('/lms/')


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/lms/')

    return render(request,'lmsapp/login.html')

#Issue Functions
# @login_required
# class IssueIndexView(generic.ListView):
#     template_name = 'lmsapp/issue/index.html'
#     context_object_name = 'issue_list'
#
#     def get_queryset(self):
#         return Issue.objects.all()

@login_required
def issue_index(request):
    context = {
        'issue_list':Issue.objects.all()
    }
    return render(request,'lmsapp/issue/index.html',context)


@login_required
def issue_new(request):
    if request.method=='POST':
        form = IssueCreateForm(request.POST or None)
        if form.is_valid():
            #Does not take care in to account is book was issued previously
            #Does not check number of available books
            #You can correct these in the code as this is barebone project
            instance = form.save(commit=False)
            instance.issued_date = datetime.now().date()
            instance.issued_by = User.objects.get(pk=request.user.id)
            instance.due_date = (datetime.now()+timedelta(days=30)).date()
            instance.save()
            instance.book.available = instance.book.available - 1
            instance.book.save()
            messages.success(request,'New Issue Created',extra_tags='alert-success')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Form is invalid",extra_tags='alert-error')
    else:
        form = IssueCreateForm()
    return render(request, 'lmsapp/issue/add.html', {'form': form})


#Book Functions
# @login_required
# class BookIndexView(generic.ListView):
#     template_name = 'lmsapp/book/index.html'
#     context_object_name = 'book_list'
#
#     def get_queryset(self):
#         return Book.objects.all()

@login_required
def book_index(request):
    context = {
        'book_list':Book.objects.all()
    }
    return render(request,'lmsapp/book/index.html',context)


@login_required
def book_new(request):
    form = BookCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'New Book Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Form is invalid")

    return render(request, 'lmsapp/book/add.html', {'form': form})

@login_required
def book_detail(request,id=None):
    instance = get_object_or_404(Book,id=id)
    context = {
    'title':instance.title,
    'price':instance.price,
    'isbn':instance.isbn,
    'authors':instance.authors,
    'publisher':instance.publisher,
    'publication_date':instance.publication_date,
    'available':instance.available

    }
    return render(request,"lmsapp/book/detail.html",context)

@login_required
def book_update(request,id=None):
    instance = get_object_or_404(Book,id=id)
    form = BookCreateForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Book Updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Form is invalid")
    context = {
    'title':instance.title,
    'price':instance.price,
    'isbn':instance.isbn,
    'authors':instance.authors,
    'publisher':instance.publisher,
    'publication_date':instance.publication_date,
    'available':instance.available,
    'form':form
    }
    return render(request,"lmsapp/book/edit.html",context)
@login_required
def book_delete(request,id=None):
    instance = get_object_or_404(Book,id=id)
    instance.delete()
    messages.success(request,"Successully deleted")
    # return HttpResponseRedirect(instance.get_absolute_url())
    return redirect('book.index')

#Author Functions
# @login_required
# class AuthorIndexView(generic.ListView):
#     template_name = 'lmsapp/author/index.html'
#     context_object_name = 'author_list'
#
#     def get_queryset(self):
#         return Author.objects.all()

@login_required
def author_index(request):
    context = {
        'author_list':Author.objects.all()
    }
    return render(request,'lmsapp/author/index.html',context)


@login_required
def author_new(request):
    if request.method == 'POST':

        form = AuthorCreateForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'New Author Created',extra_tags='alert-success')
            return render(request,'lmsapp/author/add.html',{'form':form})
        else:
            messages.error(request,"Form is invalid",extra_tags='alert-danger')
    else:
        form = AuthorCreateForm()
    return render(request, 'lmsapp/author/add.html', {'form': form})

@login_required
def author_detail(request,id=None):
    instance = get_object_or_404(Author,id=id)
    context = {
    'name':instance.name,
    'email':instance.email,

    }
    return render(request,"lmsapp/author/detail.html",context)

@login_required
def author_update(request,id=None):
    instance = get_object_or_404(Author,id=id)
    if request.method == 'POST':
        form = AuthorCreateForm(request.POST or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,'Author Updated')
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Form is invalid")
    else:

        form = AuthorCreateForm()

    context = {
    'name':instance.name,
    'email':instance.email,
    'form':form
    }
    return render(request,"lmsapp/author/edit.html",context)

@login_required
def author_delete(request,id=None):
    instance = get_object_or_404(Author,id=id)
    instance.delete()
    messages.success(request,"Successully deleted")
    # return HttpResponseRedirect(instance.get_absolute_url())
    return redirect('author.index')




#Publisher Functions
# @login_required
# class PublisherIndexView(generic.ListView):
#     template_name = 'lmsapp/publisher/index.html'
#     context_object_name = 'publisher_list'
#
#     def get_queryset(self):
#         return Publisher.objects.all()

@login_required
def publisher_index(request):
    context = {
        'publisher_list':Publisher.objects.all()
    }
    return render(request,'lmsapp/publisher/index.html',context)

@login_required
def publisher_new(request):
    form = PublisherCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'New Publisher Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Form is invalid")

    return render(request, 'lmsapp/publisher/add.html', {'form': form})

@login_required
def publisher_detail(request,id=None):
    instance = get_object_or_404(Publisher,id=id)
    context = {
    'name':instance.name,
    'address':instance.address,
    'city':instance.city,
    'state':instance.state,
    'country':instance.country,
    'website':instance.website
    }
    return render(request,"lmsapp/publisher/detail.html",context)

@login_required
def publisher_update(request,id=None):
    instance = get_object_or_404(Publisher,id=id)
    form = PublisherCreateForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Publisher Updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Form is invalid")
    context = {
    'name':instance.name,
    'address':instance.address,
    'city':instance.city,
    'state':instance.state,
    'country':instance.country,
    'website':instance.website,
    'form':form
    }
    return render(request,"lmsapp/publisher/edit.html",context)

@login_required
def publisher_delete(request,id=None):
    instance = get_object_or_404(Publisher,id=id)
    instance.delete()
    messages.success(request,"Successully deleted")
    # return HttpResponseRedirect(instance.get_absolute_url())
    return redirect('publisher.index')

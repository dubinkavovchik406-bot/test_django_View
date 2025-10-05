from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post, Author

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts_list": posts
    }
    return render(
        request,
        "myapp/post_list.html",
        context=context
    )
def get_post_by_id(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(
        request,
        "myapp/post_details.html",
        context=context
    )

def author_list(request):
    authors = Author.objects.all()
    context = {
        "authors_list": authors
    }
    return render(
        request,
        "myapp/author_list.html",
        context=context
    )

def get_author_by_id(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author
    }
    return render(
        request,
        "myapp/author_details.html",
        context=context
    )

def test(request):
    return HttpResponse("Це тестова заглушка.", status=200)
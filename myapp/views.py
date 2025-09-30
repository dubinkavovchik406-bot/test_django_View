from django.shortcuts import render
from myapp.models import Post

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

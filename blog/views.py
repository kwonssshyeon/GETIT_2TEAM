from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts':posts
        }
    )

def single_post_page(requests, pk):
    post = Post.objectsget(pk = pk)

    return render(
        requests,
        'blog/single_post_page.html',
        {
            'post':post
        }
    )
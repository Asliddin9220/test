from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.image)
    return render(request,'post_list.html', {'posts':posts})
# Create your views here.

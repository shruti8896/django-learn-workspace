from django.shortcuts import render

# Create your views here.
def starting_page(requests):
    return render(requests,"my_blogs/index.html")

def posts(requests):
    return render(requests,"my_blogs/all-posts.html",{})

def post_detail(requests,slug):
    return render(requests,"my_blogs/post-detail.html")

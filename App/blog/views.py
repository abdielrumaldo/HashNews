from django.shortcuts import render
from django.http import HttpResponse

# dummy data
posts = [
    {
        'author': "Abe",
        'title': 'Blog Post 1',
        'contents': "First Post",
        'date_posted': "August 27, 2020"
    },
    {
        'author': "Not Abe",
        'title': 'Blog Post 2',
        'contents': "Second Post",
        'date_posted': "August 28, 2020"
    },
    {
        'author': "Abe",
        'title': 'Blog Post 3',
        'contents': "Last and final Post",
        'date_posted': "August 29, 2020"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

from django.shortcuts import render


posts=[
    {
        'author':'sanix',
        'title':'life is a bitch !',
        'content':'Nobody knows is last day',
        'date_posted':'August 21, 2018'
    },
    {
        'author':'Nixa',
        'title':'Life is good ',
        'content':'Life is really good',
        'date_posted':'September 21, 2018'
    }   
]

def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')  


# Create your views here.

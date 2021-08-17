
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

# model
#from posts.models import User

posts = [
    {
        'name': 'fabian',
        'user': 'test user',
        'timestamp': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }
]


def list_posts(request):
    # user = User(name='test', passsword='123', surname='bgf')
    # user.save()
    # print(user)
    return render(request, 'feed.html', {'posts': posts})

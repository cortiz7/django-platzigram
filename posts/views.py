#Django
from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from datetime import datetime

# Create your views here.

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yessica Cortez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?=1037'
    },
    {
        'name': 'Dark Line',
        'user': 'Julio Contreras',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?=1045'
    },
    {
        'name': 'Green Gold',
        'user': 'Pedro Martinez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'http://picsum.photos/200/200/?=1058'
    }
]

def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
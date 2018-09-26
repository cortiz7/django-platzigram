""" Django """
from django.http import HttpResponse

""" Utilities """
from datetime import datetime
import json


def hello_word(request):
    return HttpResponse('Current Server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_int = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Integers sorted succefully' 
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry, {} you are not allowed here'.format(name)
    else:
        message = 'Hello, {} Welcome to Platzigram'.format(name)
    return HttpResponse(message)
    
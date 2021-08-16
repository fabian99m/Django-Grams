from django.http import HttpResponse
from django.http import JsonResponse

def hola(request):
    return HttpResponse('hola soy fabi')

def fecha(request):
    array = sorted([int(i) for i in request.GET['numbers'].split(',')])
    return JsonResponse(
            { 'numbers': str(array) }
        )

def sayhi(request,name,age):
    return HttpResponse(f'Hi {name}, your age is {age}')
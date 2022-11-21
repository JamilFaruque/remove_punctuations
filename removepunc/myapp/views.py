from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    return render(request,'home.html')

def analyze(request):
    result = ""
    t = ""
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    txt = request.GET.get('text')
    removepunc = request.GET.get('removepunc', 'off')
    allcaps = request.GET.get('allcaps','off')
    charcount = request.GET.get('charcount','off')

    if removepunc == 'on' and allcaps == 'on':

        for char in txt:
            if char not in punc:
                result = result + char.upper()

    elif removepunc == 'on':
        for char in txt:
            if char not in punc:
                result = result + char

    elif allcaps == 'on':
        for char in txt:
            result = result + char.upper()

    elif charcount == 'on':
        for char in txt:
            if char != ' ':
                t = t + char
                result = len(t)
    else:
        return HttpResponse('PLEASE CHOOSE AN OPTION')
    param = {'analyzed': result }
    return render(request, 'result.html', param )
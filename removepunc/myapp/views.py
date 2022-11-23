from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    return render(request,'home.html')

def analyze(request):
    t = ""
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    count = ""
    txt = request.GET.get('text')
    removepunc = request.GET.get('removepunc', 'off')
    allcaps = request.GET.get('allcaps','off')
    charcount = request.GET.get('charcount','off')

    # if removepunc == 'on' and allcaps == 'on':

    #     for char in txt:
    #         if char not in punc:
    #             result = result + char.upper()

    if removepunc == 'on':
        result = ""
        for char in txt:
            if char not in punc:
                result = result + char
        txt = result

    if allcaps == 'on':
        result = ""
        for char in txt:
            result = result + char.upper()
        txt = result

    if charcount == 'on':
           
        for char in txt:
            if char != ' ':
                t = t + char
                count = "---" + str(len(t)) + " characters "
        
    if removepunc == 'off' and allcaps=='off' and charcount=='off':
        return HttpResponse("PLEASE CHOOSE AN OPTION")
    param = {'analyzed': result , 'count':count }
    return render(request, 'result.html', param )
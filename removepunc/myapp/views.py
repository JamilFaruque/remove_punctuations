from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request,'home.html')

def analyze(request):
    result = ""
    punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    txt = request.GET.get('text')
    for char in txt:
        if char not in punc:
            result = result + char
    param = {'analyzed': result }
    return render(request, 'result.html', param )
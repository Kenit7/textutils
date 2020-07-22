# This Is Made By Kenit--
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Kenit</h1>''')


def analyze(request):
    # Getting Text
    djr = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)
    print(djr)
    if removepunc == "on":
        # analyzed=djr
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        for char in djr:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyzing Text
        return render(request, 'analyze.html', params)

    elif fullcap == "on":
        analyzed = ""
        for char in djr:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Full Capitalized', 'analyzed_text': analyzed}
        # Analyzing Text
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        analyzed = len(djr)
        params = {'purpose': 'Counting Of Character', 'analyzed_text': analyzed}
        # Analyzing Text
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("Cap First")
#
# def newlinerremove(request):
#     return HttpResponse("new liner remove")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
# def charcount(request):
#     return HttpResponse("Char count")

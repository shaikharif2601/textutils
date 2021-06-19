# This is my first website - Arif
from typing import Counter
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')
    numberremover=request.POST.get('numberremover', 'off')

    if (removepunc == "on"):
        punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        try:
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
        except Exception as ex:
            print(ex)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (extraspaceremover == "on"):
        analyzed = ""
        try:
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char
            params = {'purpose': 'Extra space remove', 'analyzed_text': analyzed}
            djtext = analyzed
        except Exception as ex:
            print(ex)

    if (charcount == "on"):
        analyzed = ""
        try:
            analyzed = print(Counter(djtext))
            params = {'purpose': 'Extra space remove', 'analyzed_text': analyzed}
            djtext = analyzed
        except Exception as ex:
            print(ex)

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'
        try:
            for char in djtext:
                if char not in numbers:
                    analyzed = analyzed + char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed
        except Exception as ex:
            print(ex)

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount != "on" and numberremover == "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

#i created this

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def analyze(request):
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')

    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext= analyzed


    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'In Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed


    if  newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed+char
        params = {'purpose': 'Line Removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if extraspaceremover=='on':
        analyzed = ""
        for char in djtext:
            if char != "\t":
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcounter=='on':
        analyzed =0
        for char in djtext:
                analyzed += 1
        params = {'purpose': 'CHaracter Count', 'analyzed_text': analyzed}
        djtext=analyzed





    if removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on':
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)








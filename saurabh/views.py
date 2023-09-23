from django.http import  HttpResponse
from django.shortcuts import render

# day6 tutorial
# def index(request):
#     # return HttpResponse("hrlkdvs")
#       return HttpResponse(''' "hrlkdvs",<a href="/about">about</a> ''')

# def about(request):
#     return HttpResponse("this is about routes")

def index(request):
    params = { 'name':"harry", 'place':'mars'}
    return render(request,"index.html", params)

# def about(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyse the text
#     return HttpResponse("this is about routes")

# only get request is here
# def analyze(request):
#     djtext = request.GET.get('text', 'default')
#     print("djtext", djtext)
#     removepunc = request.GET.get('removepunc', 'off')
#     fullcaps = request.GET.get('fullcaps', 'off')
#     newlineremover = request.GET.get('newlineremover', 'off')
#     spaceremover = request.GET.get('spaceremover', 'off')
#     print("removepunc", removepunc)
#     # analyse the text
#     if removepunc == "on":
#         analyzed = ""
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed =  analyzed + char

#         params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)

#     elif fullcaps=='on':
#         analyzed=''
#         for char in djtext:
#             analyzed =  analyzed + char.upper()

#         params = {'purpose': "making characters in uppercase", 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)        

#     elif (newlineremover=='on'):
#         analyzed=''
#         for char in djtext:
#             if char !="\n":
#                 analyzed =  analyzed + char

#         params = {'purpose': "removed new lines", 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params) 

#     elif spaceremover=='on':
#         analyzed=''
#         for index,char in enumerate(djtext):
#             if  not(djtext[index]==" " and djtext==' '):
#                 analyzed = analyzed + char

#         params = {'purpose': "removed new lines", 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params) 

#     else:
#         return HttpResponse("with remove punc -error")    


def analyze(request):
    djtext = request.POST.get('text', 'default')
    print("djtext", djtext)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    print("removepunc", removepunc)
    print("newlineremover", newlineremover)
    # analyse the text
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed =  analyzed + char

        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed =  analyzed + char.upper()

        params = {'purpose': "making characters in uppercase", 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)        

    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if  not(djtext[index]==" " and djtext==' '):
                analyzed = analyzed + char

        params = {'purpose': "removed new lines", 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")    

        
    return render(request, 'analyze.html', params) 

   

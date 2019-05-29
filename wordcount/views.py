from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def result(request):
    text=request.GET['fulltext']
    words=text.split(' ')
    dic={}
    for word in words:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1

    return render(request, 'result.html', {'text':text, 'size': len(words), 'dic':dic.items()})


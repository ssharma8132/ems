from django.shortcuts import render

def index(request):
    context = {}
    context['title'] = 'polls'
    return render(request, 'poll/index.html',context)

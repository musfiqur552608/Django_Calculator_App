from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
   return render(request, 'index.html')

def submitquery(request):
   q = request.GET['query']
   try:
      ans = eval(q)
      dict = {
         "q": q,
         "ans": ans,
         "error": False
      }
      return render(request, 'index.html', context = dict)
   except:
      dict = {
         "error" : True
      }
      return render(request, 'index.html', context = dict)


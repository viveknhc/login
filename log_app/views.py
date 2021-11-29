from django.shortcuts import render

# Create your views here.
def logfn(request):
    return render(request,"log.html")
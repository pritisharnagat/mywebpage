from django.shortcuts import render
from django.http import HttpResponse
from english.models import English
# Create your views here.
def english(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        english=English(firstname=firstname,lastname=lastname)
        english.save()
    return render(request,"home.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
     return render(request,"contact.html")
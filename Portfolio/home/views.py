from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is home")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is about")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is projects")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("This is contact")
    return render(request, 'contact.html')
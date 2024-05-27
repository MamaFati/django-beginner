from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world, i'm soo exited")

def about(request):
    return HttpResponse("My name is Fati and i love this")
# creating dynamic url in veiw
def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def my_age(request, name, age):
    return HttpResponse(f"Hello {name}! your are {age} years old welcome")
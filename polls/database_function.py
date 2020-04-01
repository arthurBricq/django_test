from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models

# from .models import Company


# Test for the app

# Companies have names and different services, we want to be able to retrieve this from a special link

class Company(models.Model):
    name = models.CharField(max_length=200)

class Service(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

def get_request(request):
    """
    This method shows how to use GET urls to send data
    Call the following url to send data into the server
    http://192.168.5.62:8000/polls/test_get?a=2&b=2
    """
    a = float(request.GET['a'])
    b = float(request.GET['b'])
    s = "The sum of {} and {} is {}".format(a, b, a + b)
    return HttpResponse(s)

@csrf_exempt
def get_post(request):
    """
    This method shows how to use GET urls to send data
    Call the following url to send data into the server
    http://192.168.5.62:8000/polls/test_post?a=2&b=2
    """
    # id = request.POST["id1"]
    # name = request.POST["name"]
    print(request.POST)
    return HttpResponse("POST is received")

def handle_database_view(request):
    # This page should list all the existing companies
    allCompanies = Company.objects.all()
    s = ""
    for c in allCompanies:
        s += c.name + "  -  "
    print(s)
    return HttpResponse("All companies : " + s)
    
    
def create_company_view(request, name):
    c = Company(name = name)
    c.save()
    return HttpResponse("Company " + name + " was created")

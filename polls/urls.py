from django.urls import path
from . import views
import numpy as np
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def get_request(request): 
    """
    This method shows how to use GET urls to send data
    Call the following url to send data into the server
    http://192.168.5.62:8000/polls/test_get?a=2&b=2
    """
    a = float(request.GET['a'])
    b = float(request.GET['b'])
    s = "The sum of {} and {} is {}".format(a, b, a+b)
    return HttpResponse(s)
    
@csrf_exempt
def get_post(request):
    """
    This method shows how to use GET urls to send data
    Call the following url to send data into the server
    http://192.168.5.62:8000/polls/test_post?a=2&b=2
    """
    #id = request.POST["id1"]
    #name = request.POST["name"]
    print(request.POST)
    return HttpResponse("POST is received")
    
    
    
    

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # Testing GET and POS http request to send data IN the server from remote devices
    path('test_get/', get_request),
    path('test_post/', get_post)
]

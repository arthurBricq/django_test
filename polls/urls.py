from django.urls import path
from . import views, database_function
import numpy as np

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # Testing GET and POS http request to send data IN the server from remote devices
    path('test_get/', database_function.get_request),
    path('test_post/', database_function.get_post),
    # Testing a new database for the app
    path('see_database/',database_function.handle_database_view),
    path('create_company/<slug:name>', database_function.create_company_view)
]

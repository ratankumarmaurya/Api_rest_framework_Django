import requests
from django.shortcuts import render


def show(request):
    response=requests.get('http://127.0.0.1:8000/api/basic/')
    todos=response.json()
    return render(request,'show.html', {'user':todos})

# def show (requests):
#     response=requests.get('http://127.0.0.1:8000/api/basic/')
#     todos=response.json()
#     # return render(request,'show.html',{'user':todos})
#     return render(request,'show.html',{'user':todos})

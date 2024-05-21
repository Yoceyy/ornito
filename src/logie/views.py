#Import Python

#Django import

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

#humoov import

#Public Views

def public_views (request):

    #Get me as the user
    me = request.user

    #Variable test
    hello = "welcome to Moha"

    #Context variable for the html
    context = {
        'momo' : hello
    }

    return render (request, "index.html", context)


    
    
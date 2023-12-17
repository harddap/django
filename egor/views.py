from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fullname(request, name, username):
    return HttpResponse(
        f'''<h1>name: {name}</h1><br>username: {username}'''
    )


def age(request, age_):
    return HttpResponse(
        f'''<h1>age: {age_}</h1>'''
    )


def interesting(request, int_):
    return HttpResponse(
        f'''<h1>interesting: {int_}</h1>'''
    )


def about(request, number):
    return HttpResponse(
        f'''<h1>interesting: {number}</h1>'''
    )


def contact(request, contacts):
    return HttpResponse(
        f'''<h1>interesting: {contacts}</h1>'''
    )






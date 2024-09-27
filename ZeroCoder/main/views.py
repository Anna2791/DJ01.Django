from django.shortcuts import render
from django.http import HttpResponse


def datatext(request):
    return HttpResponse("<h1>Это мой первый проект на Django!УРА</h1>")


def testtext(request):
    return HttpResponse("<h1>Это вторая страница на Django!</h1>")


def index(request):
    return HttpResponse("<h1>Это главная страница на Django!</h1>")


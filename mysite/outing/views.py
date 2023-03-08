from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'latest_question_list': 'ok',
    }
    return render(request, 'outing/index.html', context)


def json(request):
    return HttpResponse("Hello, JSON. You're at the outing index.")

from django.http import HttpResponse
from django.shortcuts import render


def tpl(request):
    context = {
        'latest_question_list': 'ok',
    }
    return render(request, 'outing/index.html', context)


def json(request):
    return HttpResponse("Hello, world. You're at the outing index.")

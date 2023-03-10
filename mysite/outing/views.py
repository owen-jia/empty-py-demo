from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
import logging
from .models import Article
import datetime
import json


logger = logging.getLogger(__name__)


def index(request):
    article_all = Article.objects.all()
    a_json = list(article_all.values())
    context = {
        'latest_question_list': 'ok',
        'article_all': a_json
    }
    return render(request, 'outing/index.html', context)


def json_return(request):
    return HttpResponse("hello, JSON. You're at the outing index.")


def form_save(request):
    """保存"""

    param = json.loads(request.body.decode())
    print(param)
    print(param.get("title"))
    print(param.get("content"))

    if request.method == 'POST':
        article_obj = Article(param.get("title"), param.get("content"), datetime.date.today())
        article_obj.save()

        article_raw = Article.objects.raw('select * from Article')
        print(article_raw)

        article_all = Article.objects.filter(title=param.get("title"))[:1]
        data = (list(article_all.values()))

        result = {
            'code': 200,
            'message': 'success',
            'data': data
        }
        return JsonResponse(result, safe=False)
    else:
        return HttpResponse({"status": "failure"}, content_type='application/json; charset=utf-8')


def form_delete(request):
    param = json.loads(request.body.decode())
    print(param)
    if request.method == 'POST':
        Article.objects.get(title=param.get("title")).delete()
        result = {
            'code': 200,
            'message': 'success',
            'data': None
        }
        return JsonResponse(result, safe=False)
    else:
        return HttpResponse({"status": "failure"}, content_type='application/json; charset=utf-8')

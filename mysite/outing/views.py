from django.http import HttpResponse
from django.shortcuts import render
import logging
from .models import Article
import datetime


logger = logging.getLogger(__name__)


def index(request):
    context = {
        'latest_question_list': 'ok',
    }
    return render(request, 'outing/index.html', context)


def json(request):
    return HttpResponse("hello, JSON. You're at the outing index.")


def form_save(request):
    logger.warning(request)
    logger.info(request.method)
    logger.debug(request.method)
    logger.error(request.method)
    if request.method == 'POST':
        article_obj = Article("今日最牛大外宣", "内容本身就很牛", datetime.date)
        print(article_obj)
        print(request.method)
        logger.info(article_obj)
        return HttpResponse({"status ok"})
    else:
        return HttpResponse({"status failure"})

from django.http import HttpResponse
from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def index(request):
    context = {
        'latest_question_list': 'ok',
    }
    return render(request, 'outing/index.html', context)


def json(request):
    return HttpResponse("Hello, JSON. You're at the outing index.")


def form_save(request):
    logger.warning(request)
    logger.info(request.method)
    logger.debug(request.method)
    logger.error(request.method)
    if request.method == 'POST':
        return HttpResponse({"status ok"})
    else:
        return HttpResponse({"status failure"})

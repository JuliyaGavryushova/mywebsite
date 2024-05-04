import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html = '<h1>Главная</h1><p>Главная страница сайта</p>'
    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    html = '<h1>Обо мне</h1><p>Здесь представлена информация обо мне</p>'
    return HttpResponse(html)

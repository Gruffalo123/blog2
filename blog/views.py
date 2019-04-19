from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Article

def hello_world(request):
    return HttpResponse("Hello world!")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%s,brief_content:%s,content:%s,article_id:%s,publish_date:%s'%(title,brief_content,
                                                                                       content,article_id,
                                                                                       publish_date)

    return HttpResponse(return_str)
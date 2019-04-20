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


#博客主页面
def get_index_page(request):
    all_article = Article.objects.all()
    return render(request,'blog/index.html',{'article_list':all_article})


#文章详情页
def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    current_article = None
    for article in all_article:
        if article.article_id == article_id:
            current_article = article
            break
    #将文章内容一段一段展示出来，不然文章是挤在一起，很不美观
    section_list = current_article.content.split('\n')
    return render(request,'blog/detail.html',{'current_article':current_article,
                                              'section_list':section_list})
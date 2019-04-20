from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Article
from django.core.paginator import Paginator

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
    #获取到的当前页面数字 index?page=(1,2,3...)
    curr_page_num = request.GET.get('page')
    if curr_page_num:
        curr_page_num = int(curr_page_num)
    else:
        curr_page_num = 1
    print('page_num:',curr_page_num)

    all_article = Article.objects.all()
    #对列表分成3页
    p = Paginator(all_article,3)
    print('page_count',p.num_pages)
    #总的页面数量,
    page_count = p.num_pages
    #当前分页页面的内容
    page_article_list = p.page(curr_page_num)
    if page_article_list.has_next():
        next_page_num = curr_page_num + 1
    else:
        next_page_num = curr_page_num

    if page_article_list.has_previous():
        previous_page_num = curr_page_num - 1
    else:
        previous_page_num = curr_page_num



    return render(request,'blog/index.html',{'article_list':page_article_list,
                                             'page_num':range(1,page_count + 1),
                                             'current_page_num':curr_page_num,
                                             'previous_page_num':previous_page_num,
                                             'next_page_num':next_page_num})


#文章详情页
def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    # current_article = None

    for index,article in enumerate(all_article):
        if index == 0:
            previous_index = index
            next_index = index + 1
        elif index == len(all_article) -1 :
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        # previous_article = all_article[previous_index]
        # next_article = all_article[next_index]

        if article.article_id == article_id:
            current_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    #将文章内容一段一段展示出来，不然文章是挤在一起，很不美观
    section_list = current_article.content.split('\n')
    return render(request,'blog/detail.html',{'current_article':current_article,
                                              'section_list':section_list,
                                              'previous_article':previous_article,
                                              'next_article':next_article})
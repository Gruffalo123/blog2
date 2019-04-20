from django.urls import path,include

import blog.views as bv

urlpatterns = [
    path('hello_world',bv.hello_world),
    path('content',bv.article_content),
    path('index',bv.get_index_page),
    # path('detail',bv.get_detail_page)
    path('detail/<int:article_id>',bv.get_detail_page)
]
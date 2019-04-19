from django.urls import path,include

import blog.views as bv

urlpatterns = [
    path('hello_world',bv.hello_world),
    path('content',bv.article_content),
]
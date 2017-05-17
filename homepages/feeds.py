# 创建订阅
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostFeed(Feed):
    title = 'My blog'  #title，link，description属性分别对应RSS的<title>，<link>，<description>元素
    link = '/homepages/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
from blog import models
from blog.models import Category


def recent_articles(request):
    recent_articles = models.Article.objects.all().order_by('-created', '-updated')[:3]
    return {'recent_articles': recent_articles}


def category_list(request):
    category = Category.objects.all().order_by('-created')
    return {"category": category}

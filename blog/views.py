from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView
from .models import Article, Category, Comment, ContactUs, Like
from .forms import ContactUsForm
from django.urls import reverse_lazy, reverse


# Create your views here.
class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class DetailViewPage(DetailView):
    model = Article


class ListViewPage(ListView):
    model = Article
    paginate_by = 2


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()  # به جای استفاده از article_set، از فیلد articles استفاده کنید
    return render(request, 'blog/article_list.html', {"object_list": articles})


def search(request):
    q = request.GET.get("q")
    article = Article.objects.filter(title__contains=q)
    page = request.GET.get("page")
    paginator = Paginator(article, 2)
    object_list = paginator.get_page(page)
    return render(request, 'blog/article_list.html', {"object_list": object_list})


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        text = request.POST.get("text")

        Comment.objects.create(text=text, article=article, author=request.user, parent_id=parent_id)

    is_liked = False
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(article=article, user_id=request.user.id).exists()

    return render(request, 'blog/article_detail.html', {'article': article, "is_liked": is_liked})


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = "blog/contactus.html"
    success_url = "/"

    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)

        return super().form_valid(form)


def about_us(request):
    return render(request, 'blog/aboutus.html', {})


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({"response": "unliked"})
        except:
            Like.objects.create(user_id=request.user.id, article_id=pk)
            return JsonResponse({"response": "liked"})

    return redirect('account:login')

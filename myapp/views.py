from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.db.models import Q
from django.shortcuts import redirect
from .forms import CommentForm

from .models import Article
from .models import Category
from .models import Tag
from .models import Comment
#from .models import PopularPost

def index(request):
    latest_category_list = Category.objects.order_by#("-pub_date")[:5]
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {"latest_category_list" : latest_category_list,
               "latest_article_list": latest_article_list
               }

    return render(request, "myapp/index.html", context)

def search(request):
    query = request.GET.get('q')
    articles = []
    categories = []
    tags = []
    comment = []

    if query:
        articles = Article.objects.filter(headline__icontains=query)
        categories = Category.objects.filter(full_name__icontains=query)
        tags = Tag.objects.filter(tag_text__icontains=query)
        comment = Comment.objects.filter(content__icontains=query)

    return render(request, 'search_results.html', {
        'articles': articles,
        'categories': categories,
        'tags': tags,
        'comments': comment,
        'query': query
    })

def search_results(request):
    query = request.GET.get('q')
    results = Article.objects.filter(content__icontains=query)
    return render(request, 'myapp/search_results.html', {'results': results})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    
    return render(request, 'myapp/article_detail.html', {'article': article, 'comments':comments, 'form': form})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'myapp/category_detail.html', {'category': category})

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'myapp/tag_detail.html', {'tag': tag})

def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'myapp/comment_detail.html', {'comment': comment})

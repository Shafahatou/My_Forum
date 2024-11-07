from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import search, comment_detail, article_detail

from . import views

urlpatterns = [
   
    path('', views.index, name='index'),

    path('search/', views.search_results, name='search_results'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('tag/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


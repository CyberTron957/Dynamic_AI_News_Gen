from django.urls import path
from . import views

urlpatterns = [
    path('', views.init_view, name = 'enter_pincode'),
    path('upload/', views.upload_and_generate, name='upload_and_generate'),
    path('Allnews/', views.news_view, name='news_view'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # New URL for article details
    path('post/new/', views.post_create, name='post-create'),
    path('generate-news/', views.generate_news, name='generate_news'), # type: ignore
    path('<str:pincode>/', views.articles_by_pincode, name='posts_by_pincode'),
    path('autocomplete/pincode/', views.autocomplete_pincode, name='autocomplete_pincode'),


]

from django.urls import path
from news import views


urlpatterns = [
    path('', views.news_page, name='news'),
    path('create', views.create_news, name='create_news'),
    path('<int:id>', views.news_detail, name='news_detail'),
    path('delete/<int:id>', views.delete_news, name='delete_news'),
    path('edit/<int:id>', views.edit_news, name='edit_news')
]

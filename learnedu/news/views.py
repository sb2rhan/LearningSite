from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewsForm
from .models import News


def news_page(request):
    context = {
        'form': NewsForm(),
        'news': News.objects.all()
    }
    return render(request, 'news/main_news.html', context)


@login_required(login_url='/auth/login')
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            unews = form.save(commit=False)
            unews.author = request.user
            unews.save()
            form.save_m2m()
        else:
            print('Create form is not valid')

    return redirect('news')


@login_required(login_url='/auth/login')
def news_detail(request, id):
    n = News.objects.get(pk=id)
    context = {
        'news': n,
        'form': NewsForm(instance=n)
    }
    return render(request, 'news/news_detail.html', context)


@login_required(login_url='/auth/login')
def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.is_active = False
    news.save()
    return redirect('news')


@login_required(login_url='/auth/login')
def edit_news(request, id):
    if request.method == 'POST':
        news = News.objects.get(pk=id)
        form = NewsForm(request.POST, request.FILES, instance=news)

        if form.is_valid():
            unews = form.save(commit=False)
            unews.author = request.user
            unews.save()
            form.save_m2m()
        else:
            print('Edit form is not valid')
    return redirect('news')

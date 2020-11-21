from django.shortcuts import render


def home_page(request):
    return render(request, 'learnedu/home_page.html')

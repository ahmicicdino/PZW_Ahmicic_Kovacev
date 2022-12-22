from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from main.models import News, Author, Category



# Create your views here.

def homepage(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, "main/news_list.html")

def authors(request):
    return render(request, "main/authors_list.html")



class HomePageView(TemplateView):
    template_name = 'index.html'


class NewsList(ListView):
    model = News
    template_name = 'news_list.html'

class AuthorsList(ListView):
    model = Author
    template_name = 'authors_list.html'

    
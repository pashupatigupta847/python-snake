from django.shortcuts import render, redirect
from news.models import News, Category, Subcribe
from news.forms import ContactUsForm, SubcribeForm, AddNewsByRepoterForm, updateNewsByRepoterForm
from django.contrib.auth.decorators import login_required

"""
home page
"""
def home_page(request):
    editorial_news = News.objects.filter(is_editorial=True).order_by("-id")[0:3]
    trending_news = News.objects.all().order_by("-views_count")[:4]
    popular_news = News.objects.all().order_by("-views_count")[:4]
    recent_news = News.objects.all().order_by("-created_date")[:3]
    editor_picks = News.objects.filter(is_editorial=True).order_by("-id")[:4]
    categories = Category.objects.all()
    category_news = {
        category.name: News.objects.filter(category=category) for category in categories
        }
    context = {
        "editorial":editorial_news,
        "trending_news": trending_news,
        "popular_news":popular_news,
        "recent_news":recent_news,
        "editor_picks":editor_picks,
        "category_news":category_news,
    }
    return render(request, "news/index.html", context)

"""

category pages
"""
def category(request, category_id):
    category_related_news = News.objects.filter(category=category_id)
    context = {
        "category_related_news":category_related_news,
    }
    return render(request, "news/category.html", context)


""" 
news detail page
"""
def detail_news(request, news_id):
    detail_news = News.objects.get(id=news_id)
    detail_news.views_count += 1
    detail_news.save()
    context = {
        "detail_news":detail_news,
    }
    return render(request, "news/details.html", context)


"""
contact us page
"""
def contact_us(request):
    form = ContactUsForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    return render(request, "news/contact.html")

"""
Subcribe  
"""
def subcribe(request):
    print("this funcation is called.....")
    form = SubcribeForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            return redirect("home_page")
        else:
            return redirect("home_page")
    except Exception as e:
        return redirect("home_page")
    return(request, "partials/footer.html")

"""
search filed 
"""
def search(request):
    if request.method == "GET":
        query = request.GET["query"]
        search_data = News.objects.filter(title__contains=query)
        data = {
            'search_data':search_data,
        }
    else:
        return redirect("homepage")
    return render(request, "news/search.html", data)

"""
repoter news list page
"""
@login_required(login_url='home_page')
def news_list(request):
    news = News.objects.filter(posted_by=request.user).order_by("-id")
    context = {
        "news":news,
    }
    return render(request, "repoter/news/list.html", context)



"""
repoter add news
"""
@login_required(login_url='home_page')
def add_news_by_repoter(request):
    context = {}
    form = AddNewsByRepoterForm(request.POST, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.save()
            return redirect("repoter_news")
    else:
        form = AddNewsByRepoterForm()
        context = {
            'form':form,
        }
        return render(request, "repoter/news/create.html", context)
    context = {
        "form":form,
    }
    return render(request, "repoter/news/create.html", context)

"""
repoter updated news
"""
@login_required(login_url='home_page')
def updated_news_by_repoter(request, id):
    context = {}
    news = News.objects.get(id=id)
    form = updateNewsByRepoterForm(request.POST, request.FILES, instance=news or None)
    if request.method == "POST":
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.save()
            return redirect("repoter_news")
    else:
        form = updateNewsByRepoterForm(instance=news)
        context = {
            'form':form,
        }
        return render(request, "repoter/news/update.html", context)
    context = {
        "form":form,
    }
    return render(request, "repoter/news/update.html", context)
        
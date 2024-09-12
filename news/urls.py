from django.urls import path
from news import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    
    path("category/<int:category_id>/", views.category, name="category"),
    path("news_detail/<int:news_id>/", views.detail_news, name="detailnews"),

    path("contact/", views.contact_us, name="contact_us"),

    path("subcribe/", views.subcribe, name="subcribe"),

    path("search/", views.search, name="search"),



    path("repoters/news/", views.news_list, name="repoter_news"),
    path("repoters/news/add", views.add_news_by_repoter, name="add_news_by_repoter"),
    path("repoters/news/<int:id>/update", views.updated_news_by_repoter, name="updated_news_by_repoter"),

]
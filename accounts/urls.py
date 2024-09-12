from django.urls import path
from accounts.views import login_page, repoter_logout
urlpatterns = [
    path('login/', login_page, name="login_page"),
    path("repoters/logout/", repoter_logout, name="logout"),
]
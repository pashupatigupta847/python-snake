from news.models import Category, Subcribe, SocialMedia


"""
News category to show in navbar
"""
def category(request):
    category = Category.objects.all()
    return {
        "category": category
    }

"""
social media
"""
def social(request):
    social = SocialMedia.objects.first()
    return {
        "social":social,
    }
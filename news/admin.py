from django.contrib import admin
from news.models import News, Category, ContactUs, Subcribe, SocialMedia

""""
this lines of codes are used to register class model into admin pannel
"""
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_date','updated_date']

@admin.register(Subcribe)
class SubcribeAdmin(admin.ModelAdmin):
    list_display = ["email","created_date","updated_date"]

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_date','updated_date']
    # readonly_fields = ["title",]
    # search_fields = ["title",]
    # list_display_links  = ['title','category']
    # list_filter = ["category",]
    # fieldsets

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone']

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display=['facebook','twitter','instagram']
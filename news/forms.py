from news.models import ContactUs, Subcribe, News
from django import forms

"""
contact us form
"""
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('first_name','last_name','email','phone','feedback_message')


"""
Subcribe form
"""
class SubcribeForm(forms.ModelForm):
    class Meta:
        model = Subcribe
        fields = ("email",)


"""
AddNewsByRepoter
"""

class AddNewsByRepoterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label =  "Select your category"
    class Meta:
        model = News
        fields = ("title","category","image","description")


class updateNewsByRepoterForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ("title","category","image","description")
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Post, Category


code_choices = [
    ("uz",_("Uzbek")),
    ("en-us",_("English")),
    ("ru",_("Russian"))
 ]

class LanguageForm(forms.Form):

    code = forms.ChoiceField(choices = code_choices)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user','title', 'content', 'categories', 'image', 'active',)

    widgets = {
        'title': forms.TextInput(attrs={'placeholder': _("Write title here")}),
        'content': forms.Textarea(attrs={'placeholder': _("Write content here")}),


    }

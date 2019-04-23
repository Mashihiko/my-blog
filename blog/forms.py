from django import forms

from .models import Post, Category

"""
CATEGORY_CHOICES = [
    (1, 'プログラミング'),
    (2, '料理'),
    (3, 'ゲーム'),
    (4, '映画'),
    (5, 'その他'),
]
"""

class PostForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
       super(PostForm, self).__init__(*args, **kwargs)
       for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

   #category = forms.ChoiceField(label='カテゴリー', choices=CATEGORY_CHOICES, initial=3)

   class Meta:
        model = Post
        fields = ('title', 'text', 'photo', 'category', )

"""
class CategoryForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
       super(PostForm, self).__init__(*args, **kwargs)
       for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

   #category = forms.ChoiceField(label='カテゴリー', choices=CATEGORY_CHOICES, initial=3)

   class Meta:
        model = Category
        fields = ('name', )

"""

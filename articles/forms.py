from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        # fields = ('title', 'content',) 이렇게 사용해도 됨
        exclude = ('user',) # 보여주지 않을 것 지정해줌. exclude
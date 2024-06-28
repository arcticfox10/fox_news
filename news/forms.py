
from django import  forms 
from .models import News
# class NewsForm(forms.Form):


    # article = forms.CharField()
    # body = forms.CharField(widget=forms.Textarea)
class NewsModelForm(forms.ModelForm):
    class Meta:
        model=News
        fields=[
            'article',
            'body'
        ]
    def clean_article(self):
        data = self.cleaned_data.get('article')
        if len(data)<5:
            raise forms.ValidationError('как можно было написать такой короткий заголовок!?!? -20 социал кредит и - кошка жена')
        return data
    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body)<50:
            raise forms.ValidationError('как можно было написать такую короткую новость!?!? -40 социал кредит и - миска рис')
        return body


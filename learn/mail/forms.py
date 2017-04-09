from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


from django.forms import formset_factory
ArticleFormSet = formset_factory(ArticleForm)
formset = ArticleFormSet()
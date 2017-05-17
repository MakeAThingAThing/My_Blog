from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder':'你的名字'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'你的邮箱'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'对方的邮箱'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

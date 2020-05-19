from django import forms
from django.contrib.auth.models import User
from bloggers.models import Blog


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}


class Post_Form(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title','desc','img')
		widgets = {'desc': forms.Textarea()}
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class signup1(forms.Form):
	username=forms.EmailField(label="Username",widget=forms.TextInput(attrs={"class":"username","id":"input1"}))
	name=forms.CharField( widget=forms.TextInput(attrs={"class":"name","id":"input1"}))
	password=forms.CharField( widget=forms.PasswordInput(attrs={"class":"password","id":"input1"}))
	password1=forms.CharField( label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"password1","id":"input1"}))
	sid=forms.CharField(widget=forms.TextInput(attrs={"class":"sid","id":"input1"}))
	token=forms.CharField(widget=forms.TextInput(attrs={"class":"token","id":"input1"}))
	mobile=forms.CharField(widget=forms.TextInput(attrs={"class":"mobile","id":"input1"}))


	def clean_username(self):
		email=self.cleaned_data.get("username")
		qs=User.objects.filter(username=email)
		if qs.exists():
			raise forms.ValidationError("Email Exists")
		return email
	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get("password")
		password1=self.cleaned_data.get("password1")
		if password1 != password:
			raise forms.ValidationError("Password must Match !")
		return data




class login1(forms.Form):
	username=forms.CharField( widget=forms.TextInput(attrs={"class":"email","placeholder":"Your Email"}))
	password=forms.CharField( widget=forms.PasswordInput(attrs={ "placeholder":"Password"}))
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')




#--------------------------------------------------------------------------------------------------------------#

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Carer First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Clients Name", "class":"form-control"}), label="")
	#Area = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Area", "class":"form-control"}), label="")
	notes = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"notes", "class":"form-control"}), label="")



   

	class Meta:
		model = Record
		exclude = ("user",)
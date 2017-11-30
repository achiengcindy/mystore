from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=False, max_length=100)
	email = forms.EmailField(required=True)
	comment = forms.CharField(widget=forms.Textarea)
	
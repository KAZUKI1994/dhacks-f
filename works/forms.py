from django import forms


class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_email(self):
		pass

class UserForm(forms.Form):
	your_name = forms.CharField(label="Your name", max_length=100)
	email = forms.CharField()
	body = forms.CharField()

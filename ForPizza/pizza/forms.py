from django import forms

class Feedback(forms.Form):
	name = forms.CharField(label='Your name:', max_length=100)
	feedback = forms.CharField(label='Your feedback:', widget=forms.Textarea, max_length=256)


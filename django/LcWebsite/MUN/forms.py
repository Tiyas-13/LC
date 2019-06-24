from django import forms

#from .models import Snippet

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	number = forms.CharField(label='Contact Number')
	committee = forms.ChoiceField(choices=[('C1','United Nations General Assembly - DISEC'),
    ('C2', 'The All India Oppostion Meet'),
    ('IPJ','International Press Journalist'),
    ('IPP', 'International Press Photographer')])
	college = forms.CharField(label='College')
	#category = forms.ChoiceField(choices=[('question','Question'), ('other', 'Other')])
	#Committee = forms.CharField(required=True)
	Past_Experience = forms.CharField(widget=forms.Textarea, required=False)
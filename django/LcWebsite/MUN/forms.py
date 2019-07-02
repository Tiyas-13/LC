from django import forms

#from .models import Snippet

class CommitteeForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	number = forms.CharField(label='Contact Number')
	committee = forms.ChoiceField(choices=[('C1','United Nations General Assembly - DISEC'),
    ('C2', 'The All India Oppostion Meet'),
    ])
	college = forms.CharField(label='College')
	Past_Experience = forms.CharField(widget=forms.Textarea, required=False)
	preference1 = forms.CharField(label='Preference_1', required=False)
	preference2 = forms.CharField(label='Preference_2', required=False)
	preference3 = forms.CharField(label='Preference_3', required=False)

class IPForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	number = forms.CharField(label='Contact Number')
	Choice = forms.ChoiceField(choices=[('IPJ','International Press Journalist'),
    ('IPP', 'International Press Photographer'),
    ])
	college = forms.CharField(label='College')
	Past_Experience = forms.CharField(widget=forms.Textarea, required=False)
	preference1 = forms.CharField(label='Preference_1', required=False)
	preference2 = forms.CharField(label='Preference_2', required=False)
	preference3 = forms.CharField(label='Preference_3', required=False)

'''('IPJ','International Press Journalist'),
    ('IPP', 'International Press Photographer')'''
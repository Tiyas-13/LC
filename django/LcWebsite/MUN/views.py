from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ContactForm
from .models import FormNew

def base(request):
	return render_to_response('MUN/base.html')

def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			#committee = form.cleaned_data['Committee']
			number = form.cleaned_data['number']
			committee = form.cleaned_data['committee']
					
			college = form.cleaned_data['college']
			exp = form.cleaned_data['Past_Experience']
			form_obj = FormNew(name = name, email = email, number=number, committee=committee, college=college, Past_Experience=exp)
			form_obj.save()
			messages.success(request, f'{name} has successfully regsitered!')
			return redirect('register')
	else:		
		form = ContactForm()
	return render(request, 'MUN/form.html', {'form': form})

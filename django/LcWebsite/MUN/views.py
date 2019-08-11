from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CommitteeForm
from .forms import IPForm
from .models import Committee1
from .models import IP1

def base(request):
	return render_to_response('MUN/base.html')

def landing(request):
	return render_to_response('MUN/landing.html')

def thank(request):
	return render_to_response('MUN/thank.html')

def committee(request):

	if request.method == 'POST':
		form = CommitteeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			number = form.cleaned_data['number']
			committee = form.cleaned_data['committee']
			p1 = form.cleaned_data['preference1']
			p2 = form.cleaned_data['preference2']
			p3 = form.cleaned_data['preference3']
			college = form.cleaned_data['college']
			exp = form.cleaned_data['Past_Experience']
			form_obj = Committee1(name = name, email = email, number=number, committee=committee, preference1=p1, preference2=p2, preference3= p3, college=college, Past_Experience=exp)
			form_obj.save()
			#messages.success(request, f'{name} has successfully regsitered!')
			return redirect('thankyou')
	else:		
		form = CommitteeForm()
	return render(request, 'MUN/form.html', {'form': form})

def ip(request):

	if request.method == 'POST':
		form2 = IPForm(request.POST)
		if form2.is_valid():
			name = form2.cleaned_data['name']
			email = form2.cleaned_data['email']
			number = form2.cleaned_data['number']
			Choice = form2.cleaned_data['Choice']
			p1 = form2.cleaned_data['preference1']
			p2 = form2.cleaned_data['preference2']
			p3 = form2.cleaned_data['preference3']
			college = form2.cleaned_data['college']
			exp = form2.cleaned_data['Past_Experience']
			form2_obj = IP1(name = name, email = email, number=number, Choice=Choice, preference1=p1, preference2=p2, preference3= p3, college=college, Past_Experience=exp)
			form2_obj.save()
			#messages.success(request, f'{name} has successfully regsitered!')
			return redirect('thankyou')
	else:		
		form2 = IPForm()
	return render(request, 'MUN/form2.html', {'form2': form2})
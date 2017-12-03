from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm
#from django.contrib import messages

def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	confirm_message = None

	
	if form.is_valid():
		name = form.cleaned_data['name']
		subject = 'message from my blog'
		comment = form.cleaned_data['comment']
		message ='%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
		title = 'Thanks'
		confirm_message = "Thanks for the message we will get right back"
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message}
	return render(request, 'contacts/contact.html', context)

	
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe

stripe.api_key=settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	if request.method =='POST':
		token = request.POST['stripeToken']
		#token = request.POST('stripeToken')
		# Get the credit card details submitted by the form
		# Charge the user's card:
		try:
			#charge(
			charge = stripe.Charge.create(
				amount = 1000,
				currency = "usd",
				description = "Example charge",
				source = token)
		except stripe.error.CardError as e:
			pass
	context = {'publishKey': publishKey}
	template = 'checkout/checkout.html'
	return render(request, template, context)




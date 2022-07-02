from email import message
import imp
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, get_connection, EmailMultiAlternatives
from ..models.models import Subscribe, Contact
# Create your views here.
from..models.forms import SubscribeForm
from smart.settings import EMAIL_HOST_USER
from django.conf import settings
from django.template import loader




def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        new_contact = Contact(name=name,subject=subject,email=email,message=message)
        new_contact.save()

    return render(request, 'index.html', )
    ...
    #projet = Product.objects.all()
    return render(request, 'index.html',#{'projet':projet}
    )


#def commande(request):
   # ...
    #projet = Product.objects.all()
 #   return render(request, 'reservation.html',#{'projet':projet}
  #  )


def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':      
        name=request.POST.get('name')
        adress=request.POST.get('adress')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        paiement=request.POST.get('paiement')
        choice=request.POST.get('choice')
        date_rv=request.POST.get('date_rv')

        #form = SubscribeForm(request.POST)
        #form.save()

        #new_book = Subscribe(name=name,adress=adress,email=email,phone=phone,paiement=paiement,choice=choice,date_rv=date_rv)
        #new_book.save()

        template=loader.get_template('reservation_sms.txt')


        form_data = {
            'name':name,
            'email':email,
            'adress':adress,
            'phone':phone,
            'choice':choice,
        }
        message=template.render(form_data)
        email = EmailMultiAlternatives("Pressing Smart", message,"smartpressing2022@gmail.com", ['ouzediop98@gmail.com',email])
        # Convert the html and css inside the [subscription_form.txt] to HTML UPDATE
        email.content_subtype='html'
        
        email.send()
        messages.success(request, "Merci !!! Votre demande a ete prise en compte. Consultez votre boite email.")
        return HttpResponseRedirect('/')

    return render(request, 'reservation.html', {'form':form})

# Create your views here.
#DataFlair #Send Email









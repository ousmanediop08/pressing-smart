from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Subscribe



class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    subject=forms.CharField(max_length=200)
    message=forms.CharField(widget=forms.Textarea)


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)

#class TimePickerInput(forms.TimeInput):
 #       input_type = 'time'

#class DateTimePickerInput(forms.DateTimeInput):
  #      input_type = 'datetime'


# Create a Susbscribe Form
class SubscribeForm(ModelForm):

    CHOICE_TYPE = [
                ('Complet','Complet'),
                ('Sec','Nettoyage à sec'),
        ]

    PAYMENT_TYPE = [
        ('Cash','Cash'),
        ('Orange Money','Orange Money'),
        ('Wave','Wave'),
    ]

    name = forms.CharField(label='Prenom', max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prenom'}))
    adress = forms.CharField(label='Adresse', max_length=30, required=True, help_text='Adresse precis',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Adresse'}))
    email = forms.EmailField(label='Email' ,max_length=125, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone = forms.IntegerField(label='Telephone' ,required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Telephone'}))
    #paiement =  forms.CharField(choices=PAYMENT_TYPE, widget=forms.RadioSelect(attrs={'class':'form-group'}))
    #paiement=forms.CharField(label='Choix de paiement',widget=forms.RadioSelect(choices=PAYMENT_TYPE,attrs={'class':'form-group'}))
    paiement = forms.ChoiceField(label='Type de paiement', choices=PAYMENT_TYPE)
    #choice = forms.CharField(choices=CHOICE_TYPE, widget=forms.RadioSelect(attrs={'class':'form-group'}))    
    choice = forms.ChoiceField(label='Type de service', choices=CHOICE_TYPE)
    #date_rv = forms.DateField(label='Date de Rendez-vous', widget=DateInput,required=False)

    class Meta:
        model=Subscribe
        fields = "__all__"
        #fields = ('name','adress','email','phone','paiement','choice','date_rv')
        widgets = {
            'choice': forms.ChoiceField(
             widget=forms.Select(attrs={'class':'form-control'})
    ),
}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["start"].widget = DateInput()
        #self.fields["end"].widget = DateInput()
        #self.fields["opening"].widget = TimeInput()
        #self.fields["closing"].widget = TimeInput()
        #self.fields["vernissage"].widget = DateTimeInput()
        #self.fields["vernissage"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        self.fields["date_rv"].widget = DateTimeInput()
        self.fields["date_rv"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        self.fields["date_rv"].label = "Date de Rendez-vous"
        


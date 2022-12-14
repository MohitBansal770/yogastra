from django import forms
TIMINGS=[
    (hash('06:00-07:00'),'06:00-07:00'),
    (hash('07:00-08:00'),'07:00-08:00'),
    (hash('08:00-09:00'),'08:00-09:00'),
    (hash('17:00-18:00'),'17:00-18:00')]
class Subscribe(forms.Form):
    email = forms.EmailField(label='Email', max_length=100,required=True)
    first_name = forms.CharField(label='First Name', max_length=100,required=True)
    last_name = forms.CharField(label='Last Name', max_length=100,required=True)
    timing=forms.IntegerField(label='Timing',widget=forms.Select(choices=TIMINGS),required=True)
    age=forms.IntegerField(label='Age',min_value=18,max_value=65,required=True)
    
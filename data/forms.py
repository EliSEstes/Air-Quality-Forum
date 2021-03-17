from django import forms

class NameForm(forms.Form):
    city_name = forms.CharField(label='City Name', max_length=100)

class NamesForm(forms.Form):
    city_name1 = forms.CharField(label='City Name 1', max_length=100)
    city_name2 = forms.CharField(label='City Name 2', max_length=100)
    city_name3 = forms.CharField(label='City Name 3', max_length=100)
    city_name4 = forms.CharField(label='City Name 4', max_length=100)
    city_name5 = forms.CharField(label='City Name 5', max_length=100)

class HoursForm(forms.Form):
	city_hour1 = forms.CharField(label='City Name', max_length=100)
	city_attr = forms.CharField(label='City Attr', max_length=100)
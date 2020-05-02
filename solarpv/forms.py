from django import forms
from .models import User, TestStandard, Client, Product
import datetime

STATES = [('AL',	'Alabama'), 
		  ('AK',	'Alaska'),
		  ('AZ',	'Arizona'),
		  ('AR',	'Arkansas'),
		  ('CA',	'California'),
		  ('CO',	'Colorado'),
		  ('CT',	'Connecticut'),
		  ('DC',	'D.C.'),
		  ('DE',	'Delaware'),
		  ('FL',	'Florida'),
		  ('GA',	'Georgia'),
		  ('HI',	'Hawaii'),
		  ('ID',	'Idaho'),
		  ('IL',	'Illinois'),
		  ('IN',	'Indiana'),
		  ('IA',	'Iowa'),
		  ('KS',	'Kansas'),
		  ('KY',	'Kentucky'),
		  ('LA',	'Louisiana'),
		  ('ME',	'Maine'),
		  ('MD',	'Maryland'),
		  ('MA',	'Massachusetts'),
		  ('MI',	'Michigan'),
		  ('MN',	'Minnesota'),
		  ('MS',	'Mississippi'),
		  ('MO',	'Missouri'),
		  ('MT',	'Montana'),
		  ('NE',	'Nebrask'),
		  ('NV',	'Nevada'),
		  ('NH',	'New Hampshire'),
		  ('NJ',	'New Jersey'),
		  ('NM',	'New Mexico'),
		  ('NY',	'New York'),
		  ('NC',	'North Carolina'),
		  ('ND',	'North Dakota'),
		  ('OH',	'Ohio'),
		  ('OK',	'Oklahoma'),
		  ('OR',	'Oregon'),
		  ('PA',	'Pennsylvania'),
		  ('RI',	'Rhode Island'),
		  ('SC',	'South Carolina'),
		  ('SD',	'South Dakota'),
		  ('TN',	'Tennessee'),
		  ('TX',	'Texas'),
		  ('UT',	'Utah'),
		  ('VT',	'Vermont'),
		  ('VA',	'Virginia'),
		  ('WA',	'Washington'),
		  ('WV',	'West Virginia'),
		  ('WI',	'Wisconsin'),
		  ('WY',	'Wyoming')]

TITLES = [('NO', '--'),
		  ('MR', 'Mr.'),
		  ('MS', 'Ms.'),
		  ('MRS', 'Mrs.'),
		  ('DR', 'Dr.')]

TYPE = [('ST', 'Staff'),
		('CL', 'Client')]

class UserForm(forms.Form):	
	user_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'username'}), max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}), max_length=30)
	client_name = forms.ModelChoiceField(queryset=Client.objects.all(), to_field_name="client_name")
	first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'fname'}), max_length=30)
	middle_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'mname'}), max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'lname'}), max_length=30)
	job_title = forms.CharField(widget=forms.TextInput(attrs={'id': 'job_title'}), max_length=30)
	prefix = forms.CharField(widget=forms.Select(attrs={'id': 'prefix'}, choices=TITLES), max_length=3)
	email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email'}), max_length=30)
	office_phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'office_phone'}), max_length=10)
	phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone'}), max_length=10)

class SignInForm(forms.Form):
	user_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'loginname'}), max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}), max_length=30)

class ProductForm(forms.Form):
	model_num = 				forms.CharField(widget=forms.TextInput(attrs={'id': 'model_num'}), max_length=30)
	product_name = 				forms.CharField(widget=forms.TextInput(attrs={'id': 'product_name'}), max_length=30)
	cell_tech = 				forms.CharField(widget=forms.TextInput(attrs={'id': 'cell_tech'}), max_length=30)
	cell_num = 					forms.CharField(widget=forms.NumberInput(attrs={'id': 'cell_num'}))
	cell_num_series = 			forms.CharField(widget=forms.NumberInput(attrs={'id': 'cell_num_series'}))
	num_series_string = 		forms.CharField(widget=forms.NumberInput(attrs={'id': 'num_series_string'}))
	num_bypass_diodes = 		forms.CharField(widget=forms.NumberInput(attrs={'id': 'num_bypass_diodes'}))
	length = 					forms.CharField(widget=forms.NumberInput(attrs={'id': 'length'}))
	width = 					forms.CharField(widget=forms.NumberInput(attrs={'id': 'width'}))
	weight = 					forms.CharField(widget=forms.NumberInput(attrs={'id': 'weight'}))
	superstrate_type =			forms.CharField(widget=forms.TextInput(attrs={'id': 'superstrate_type'}), max_length=30)
	superstrate_manufacturer =	forms.CharField(widget=forms.TextInput(attrs={'id': 'superstrate_manufacturer'}), max_length=30)
	substrate_type = 			forms.CharField(widget=forms.TextInput(attrs={'id': 'substrate_type'}), max_length=30)
	substrate_manufacturer = 	forms.CharField(widget=forms.TextInput(attrs={'id': 'substrate_manufacturer'}), max_length=30)
	frame_material = 			forms.CharField(widget=forms.TextInput(attrs={'id': 'frame_material'}), max_length=30)
	frame_adhesive = 			forms.CharField(widget=forms.TextInput(attrs={'id': 'frame_adhesive'}), max_length=30)
	encapsulant_type = 			forms.CharField(widget=forms.TextInput(attrs={'id': 'encapsulant_type'}), max_length=30)
	encapsulant_manufacturer = 	forms.CharField(widget=forms.TextInput(attrs={'id': 'encapsulant_manufacturer'}), max_length=30)
	junction_type = 			forms.CharField(widget=forms.TextInput(attrs={'id': 'junction_type'}), max_length=30)
	junction_manufacturer = 	forms.CharField(widget=forms.TextInput(attrs={'id': 'junction_manufacturer'}), max_length=30)

class ClientForm(forms.Form):
	client_name = 	 forms.CharField(widget=forms.TextInput(attrs={'id': 'client_name'}), max_length=30)
	client_type =	 forms.CharField(widget=forms.TextInput(attrs={'id': 'client_type'}), max_length=30)
	address_1 = 	 forms.CharField(widget=forms.TextInput(attrs={'id': 'address_1'}), max_length=30)
	address_2 = 	 forms.CharField(widget=forms.TextInput(attrs={'id': 'address_2'}), max_length=30)
	city = 			 forms.CharField(widget=forms.TextInput(attrs={'id': 'city'}), max_length=30)
	state = 		 forms.CharField(widget=forms.Select(attrs={'id': 'state'}, choices=STATES), max_length=2)
	zipcode = 		 forms.IntegerField(widget=forms.TextInput(attrs={'id': 'zipcode'}))
	country = 		 forms.CharField(widget=forms.TextInput(attrs={'id': 'country'}), max_length=30)
	phone_number =	 forms.CharField(widget=forms.TextInput(attrs={'id': 'phone_number'}), max_length=10)
	fax_number =	 forms.CharField(widget=forms.TextInput(attrs={'id': 'fax_number'}), max_length=20)

class TestForm(forms.Form):
	standard_name = 	forms.CharField(widget=forms.TextInput(attrs={'id': 'standard_name'}), max_length=30)
	description = 		forms.CharField(widget=forms.TextInput(attrs={'id': 'description'}), max_length=100)

class CertForm(forms.Form):
	certificate_number = forms.CharField(widget=forms.TextInput(attrs={'id': 'certificate_number'}), max_length=30)
	report_number = forms.CharField(widget=forms.TextInput(attrs={'id': 'report_number'}), max_length=30)
	user_name = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name="user_name")
	standard_id = forms.ModelChoiceField(queryset=TestStandard.objects.all(), to_field_name="standard_id")
	model_number = forms.ModelChoiceField(queryset=Product.objects.all(), to_field_name="model_number")
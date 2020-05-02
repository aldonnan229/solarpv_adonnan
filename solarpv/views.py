from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Certificate, Client, Product, TestStandard
from .forms import UserForm, SignInForm, ProductForm, ClientForm, TestForm, CertForm
from .api.views import CertificateList
from .api.serializers import CertificateSerializer
import requests

def index(request):
	form = SignInForm()
	context = {'form' : form}
	return render(request, 'index.html', context)

def register(request):
	form = UserForm()
	context = {'form' : form}
	return render(request, 'register.html', context)

def dashboard(request):
	pr_form = ProductForm()
	cl_form = ClientForm()
	test_form = TestForm()
	cert_form = CertForm()
	context = {'product' : pr_form,
			   'client' : cl_form,
			   'test' : test_form,
			   'cert' : cert_form}
	return render(request, 'dashboard.html', context)

def find_cert(request):
	return render(request, 'find_cert.html')

def create_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			try:
				user = User.objects.get(user_name=request.POST['user_name'])
				return redirect('register')
			except ObjectDoesNotExist:
				try:
					client = Client.objects.get(client_name=request.POST['client_name'])
					new_user = User(user_name=request.POST['user_name'],
									password=request.POST['password'],
									client_name=client,
									first_name=request.POST['first_name'],
									middle_name=request.POST['middle_name'],
									last_name=request.POST['last_name'],
									job_title=request.POST['job_title'],
									prefix=request.POST['prefix'],
									email=request.POST['email'], 
									office_phone=request.POST['office_phone'],
									phone=request.POST['phone'])
					new_user.save()
					return redirect('index')
				except ObjectDoesNotExist:
					return redirect('register')
		else:
			return redirect('register')


def sign_in(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)
		if form.is_valid():
			try:
				user = User.objects.get(user_name=request.POST['user_name'], password=request.POST['password'])
				if user.user_type == 'CL':
					return redirect('index')
				else:
					return redirect('dashboard')
			except ObjectDoesNotExist:
				return redirect('index')
		else:
			return redirect('index')

def product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			new_product = Product(model_number=				request.POST['model_num'],
								  product_name=				request.POST['product_name'],
								  cell_technology= 			request.POST['cell_tech'],
								  number_cells=				request.POST['cell_num'],
								  number_cells_series=		request.POST['cell_num_series'],
								  number_series=	 		request.POST['num_series_string'],
								  number_diodes=			request.POST['num_bypass_diodes'],
								  product_length= 			request.POST['length'],
								  product_width= 			request.POST['width'],
								  product_weight= 			request.POST['weight'],
								  superstrate_type=			request.POST['superstrate_type'],
								  superstrate_manufacturer=	request.POST['superstrate_manufacturer'],
								  substrate_type= 			request.POST['substrate_type'],
								  substrate_manufacturer=	request.POST['substrate_manufacturer'],
								  frame_type= 				request.POST['frame_material'],
								  frame_adhesive= 			request.POST['frame_adhesive'],
								  encapsulant_type= 		request.POST['encapsulant_type'],
								  encapsulant_manufacturer= request.POST['encapsulant_manufacturer'],
								  junction_box_type= 		request.POST['junction_type'],
								  junction_box_manufacturer=request.POST['junction_manufacturer'])
			new_product.save()
	return redirect('dashboard')

def client(request):
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			new_client = Client(client_name = 	 	request.POST['client_name'],
								client_type = 		request.POST['client_type'],
								address_1 = 		request.POST['address_1'],
								address_2 = 		request.POST['address_2'],
								city = 				request.POST['city'],	
								state = 			request.POST['state'],
								zipcode = 			request.POST['zipcode'],
								country = 			request.POST['country'],
								phone_number = 		request.POST['phone_number'],
								fax_number = 		request.POST['fax_number'])
			new_client.save()
	return redirect('dashboard')

def test_standard(request):
	if request.method == 'POST':
		form = TestForm(request.POST)
		if form.is_valid():
			new_test = TestStandard(standard_name =	 request.POST['standard_name'],
									description =	 request.POST['description'])
			new_test.save()
	return redirect('dashboard')

def certificate(request):
	if request.method == 'POST':
		form = CertForm(request.POST)
		if form.is_valid():
			user = User.objects.get(user_name=request.POST['user_name'])
			standard = TestStandard.objects.get(standard_id=request.POST['standard_id'])
			model = Product.objects.get(model_number=request.POST['model_number'])
			new_cert = Certificate(certificate_number = request.POST['certificate_number'],
								   report_number = 		request.POST['report_number'],
								   user_name = 			user,
								   standard_id = 		standard,
								   model_number = 		model);
			new_cert.save()
	return redirect('dashboard')

#DELETION
def del_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			new_product = Product.objects.get(model_number=request.POST['model_num'])
			new_product.save()
	return redirect('dashboard')

def del_client(request):
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			new_client = Client.objects.get(client_name=request.POST['client_name'])
			new_client.save()
	return redirect('index')

def del_test_standard(request):
	if request.method == 'POST':
		form = TestForm(request.POST)
		if form.is_valid():
			new_test = TestStandard.objects.get(standard_name=request.POST['standard_name'])
			new_test.save()
	return redirect('dashboard')

def del_certificate(request):
	if request.method == 'POST':
		form = CertForm(request.POST)
		if form.is_valid():
			new_cert = Certificate.objects.get(certificate_number=request.POST['certificate_number'])
			new_cert.save()
	return redirect('dashboard')
from django.db import models
import datetime

class Product(models.Model):
	model_number = models.AutoField(primary_key=True)
	product_name = models.CharField(max_length=30)
	cell_technology = models.CharField(max_length=30)
	cell_manufacturer = models.CharField(max_length=30)
	number_cells = models.IntegerField()
	number_cells_series = models.IntegerField()
	number_series = models.IntegerField()
	number_diodes = models.IntegerField()
	product_length = models.DecimalField(decimal_places=4, max_digits=30)
	product_width = models.DecimalField(decimal_places=4, max_digits=30)
	product_weight = models.DecimalField(decimal_places=4, max_digits=30)
	superstrate_type = models.CharField(max_length=30)
	superstrate_manufacturer = models.CharField(max_length=30)
	substrate_type = models.CharField(max_length=30)
	substrate_manufacturer = models.CharField(max_length=30)
	frame_type = models.CharField(max_length=30)
	frame_adhesive = models.CharField(max_length=30)
	encapsulant_type = models.CharField(max_length=30)
	encapsulant_manufacturer = models.CharField(max_length=30)
	junction_box_type = models.CharField(max_length=30)
	junction_box_manufacturer = models.CharField(max_length=30)

	def __str__(self):
		return str(self.model_number)

class Client(models.Model):
	client_id = models.AutoField(primary_key=True)
	client_name = models.CharField(max_length=30)
	client_type = models.CharField(max_length=30)
	address_1 = models.CharField(max_length=30)
	address_2 = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zipcode = models.IntegerField()
	country = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=10)
	fax_number = models.CharField(max_length=20)

	def __str__(self):
		return str(self.client_name) + " (" + str(self.client_id) + ")"

class User(models.Model):
	user_name = models.CharField(primary_key=True, default="anon", max_length=30)
	password = models.CharField(max_length=30, default="password")
	client_name = models.ForeignKey(Client, on_delete=models.CASCADE, default='company')
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	prefix = models.CharField(max_length=3)
	job_title = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	office_phone = models.CharField(max_length=10)
	phone = models.CharField(max_length=10)
	user_type = models.CharField(max_length=2, default='CL')

	def __str__(self):
		return str(self.user_name)

class Location(models.Model):
	location_id = models.AutoField(primary_key=True)
	address_1 = models.CharField(max_length=30)
	address_2 = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	postal_code = models.IntegerField()
	country = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=10)
	fax_number = models.CharField(max_length=20)
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

class TestSequence(models.Model):
	sequence_id = models.AutoField(primary_key=True)
	sequence_name = models.CharField(max_length=30)

class TestStandard(models.Model):
	standard_id = models.AutoField(primary_key=True)
	standard_name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	published_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.standard_id)

class Certificate(models.Model):
	certificate_id = models.AutoField(primary_key=True)
	certificate_number = models.CharField(max_length=30)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)
	report_number = models.IntegerField()
	issue_date = models.DateTimeField(auto_now_add=True)
	standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
	model_number = models.ForeignKey(Product, on_delete=models.CASCADE)

class Service(models.Model):
	service_id = models.AutoField(primary_key=True)
	service_name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	is_fi_required = models.BooleanField()
	fi_frequency = models.DecimalField(decimal_places=4, max_digits=30)
	standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)

class PerformanceData(models.Model):
	model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
	sequence_id = models.ForeignKey(Service, on_delete=models.CASCADE)
	max_system_voltage = models.DecimalField(decimal_places=4, max_digits=30)
	voc = models.DecimalField(decimal_places=4, max_digits=30)
	isc = models.DecimalField(decimal_places=4, max_digits=30)
	vmp = models.DecimalField(decimal_places=4, max_digits=30)
	imp = models.DecimalField(decimal_places=4, max_digits=30)
	pmp = models.DecimalField(decimal_places=4, max_digits=30)
	ff = models.DecimalField(decimal_places=4, max_digits=30)


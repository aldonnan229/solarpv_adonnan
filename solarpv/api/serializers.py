from rest_framework import serializers
from ..models import User, Product, Certificate, Service, Client, TestStandard

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'user_name',
			'password',
			'client_name',
			'first_name',
			'middle_name',
			'last_name',
			'job_title',
			'prefix',
			'email',
			'office_phone',
			'phone'
		]

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = [
			'model_number',
			'product_name',
			'cell_technology',
			'cell_manufacturer',
			'number_cells',
			'number_cells_series',
			'number_series',
			'number_diodes',
			'product_length',
			'product_width',
			'product_weight',
			'superstrate_type',
			'superstrate_manufacturer',
			'substrate_type',
			'substrate_manufacturer',
			'frame_type',
			'frame_adhesive',
			'encapsulant_type',
			'encapsulant_manufacturer',
			'junction_box_type',
			'junction_box_manufacturer'
		]

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = [
			'service_id',
			'service_name',
			'description', 
			'is_fi_required',
			'fi_frequency',
			'standard_id'
		]

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = [
			'client_id',
			'client_name',
			'client_type',
			'address_1',
			'address_2',
			'city',
			'state',
			'zipcode',
			'country',
			'phone_number',
			'fax_number'
		]

class StandardSerializer(serializers.ModelSerializer):
	class Meta:
		model = TestStandard
		fields= [
			'standard_id',
			'standard_name',
			'description',
			'published_date'
		]


class CertificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		fields = [
			'certificate_number',
			'certificate_id',
			'user_name',
			'report_number',
			'issue_date',
			'standard_id',
			'model_number'
		]
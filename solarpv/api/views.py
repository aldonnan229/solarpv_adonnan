from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Product, Certificate, Service, Client, TestStandard
from .serializers import ProductSerializer, CertificateSerializer, ServiceSerializer, ClientSerializer, StandardSerializer

#product views
class ProductList(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

#certificate views
class CertificateList(generics.ListAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class CertificateDetail(generics.RetrieveAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

#service views
class ServiceList(generics.ListAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

#service views
class ClientList(generics.ListAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

	#service views
class StandardList(generics.ListAPIView):
	queryset = TestStandard.objects.all()
	serializer_class = StandardSerializer

class StandardDetail(generics.RetrieveAPIView):
	queryset = TestStandard.objects.all()
	serializer_class = StandardSerializer
from django.urls import path
from . import views

app_name = 'solarpv'

urlpatterns = [
	path('products/', views.ProductList.as_view(), name='product_list'),
	path('products/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
	path('certificates/', views.CertificateList.as_view(), name='certificate_list'),
	path('certificates/<pk>/', views.CertificateDetail.as_view(), name='certificate_detail'),
	path('services/', views.ServiceList.as_view(), name='service_list'),
	path('services/<pk>/', views.ServiceDetail.as_view(), name='service_detail'),
	path('clients/', views.ClientList.as_view(), name='client_list'),
	path('clients/<pk>/', views.ClientDetail.as_view(), name='client_detail'),
	path('standards/', views.StandardList.as_view(), name='standard_list'),
	path('standards/<pk>/', views.StandardDetail.as_view(), name='standard_detail')
]
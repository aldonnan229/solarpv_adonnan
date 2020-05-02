from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index/', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('find_cert/', views.find_cert, name='find_cert'),
	path('create_user/', views.create_user, name='create_user'),
	path('sign_in/', views.sign_in, name='sign_in'),
	path('product/', views.product, name='product'),
	path('client/', views.client, name='client'),
	path('test_standard/', views.test_standard, name='test_standard'),
	path('certificate/', views.certificate, name='certificate'),
	path('del_product/', views.del_product, name='del_product'),
	path('del_client/', views.del_client, name='del_client'),
	path('del_test_standard/', views.del_test_standard, name='del_test_standard'),
	path('del_certificate/', views.del_certificate, name='del_certificate'),
	path('api/', include('solarpv.api.url', namespace='api'))
]
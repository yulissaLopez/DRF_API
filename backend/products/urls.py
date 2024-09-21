from django.urls import path
from products import views

urlpatterns = [
    # estoy llamndo una vista basada en clases
    path('', views.product_list_create_view, name = 'product-create'),
    path('<int:pk>/', views.product_detail_view, name = 'product-detail')
]

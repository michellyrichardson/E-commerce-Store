from django.contrib import admin
from django.urls import path
from EcommerceApp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.main),
    path('<int:id>/', views.detail),
    path('checkout/', views.checkout),
]
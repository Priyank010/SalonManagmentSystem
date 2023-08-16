"""SalonManagmentSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from MainApp.views import *
from django.urls import re_path as url

router = routers.DefaultRouter()

router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'appointment-extend', AppointmentExtendViewSet, basename='appointment_extend')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'bill', BillViewSet, basename='bill')
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'chair', ChairViewSet, basename='chair')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer-history', CustomerHistoryViewSet, basename='customer_history')
router.register(r'dead-stock', DeadStockViewSet, basename='dead_stock')
router.register(r'expense', ExpenseViewSet, basename='expense')
router.register(r'gift-card', GiftCardViewSet, basename='gift_card')
router.register(r'in-house-product-use', InHouseProductUseViewSet, basename='in_house_product_use')
router.register(r'incorporation-images', IncorporationImagesViewSet, basename='incorporation_images')
router.register(r'loyalty_point_master', LoyaltyPointMasterViewSet, basename='loyalty_point_master')
router.register(r'membership', MembershipViewSet, basename='membership')
router.register(r'membership-services', MembershipServicesViewSet, basename='membership_services')
router.register(r'offers', OffersViewSet, basename='offers')
router.register(r'other-images', OtherImagesViewSet, basename='other_images')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'purchase', PurchaseViewSet, basename='purchase')
router.register(r'salon-name', SalonNameViewSet, basename='salon_name')
router.register(r'salon-name-extend', SalonNameExtendViewSet, basename='salon_name_extend')
router.register(r'salon-owner-rights', SalonOwnerRightsViewSet, basename='salon_owner_rights')
router.register(r'salon-staff-rights', SalonStaffRightsViewSet, basename='salon_staff_rights')
router.register(r'salon-staff', SalonStaffViewSet, basename='salon_staff')
router.register(r'salon-staff-extend', SalonStaffExtendViewSet, basename='salon_staff_extend')
router.register(r'salary-and-commission', SalaryAndCommissionViewSet, basename='salary_and_commission')
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'service-history', ServiceHistoryViewSet, basename='service_history')
router.register(r'stock', StockViewSet, basename='stock')
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'stock-history', StockHistoryViewSet, basename='stock_history')
router.register(r'target', TargetViewSet, basename='target')
router.register(r'target-history', TargetHistoryViewSet, basename='target_history')
router.register(r'unit-type', UnitTypeViewSet, basename='unit_type')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    url('^accounts/login/$', LoginView.as_view(), name='login'),
    url('^accounts/logout/$', LogoutView.as_view(), name='logout'),
]

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(user)
            django_login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            context = {"email": request.data['email'],
                       "user_id": User.objects.get(email=request.data['email']).id,
                       "owner": User.objects.get(email=request.data['email']).owner,
                       "staff": User.objects.get(email=request.data['email']).staff,
                       'token': token.key}
        else:
            context = {"error_msg": serializer.errors['non_field_errors'][0]}
        return Response(context, status=200)
    
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

class IncorporationImagesViewSet(viewsets.ModelViewSet):
    queryset = IncorporationImages.objects.all()
    serializer_class = IncorporationImagesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class OtherImagesViewSet(viewsets.ModelViewSet):
    queryset = OtherImages.objects.all()
    serializer_class = OtherImagesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class SalonNameViewSet(viewsets.ModelViewSet):
    # queryset = SalonName.objects.all()
    serializer_class = SalonNameSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','user','url_slug','gstin','dev_only','active']
    def get_queryset(self):
        queryset = SalonName.objects.all()
        name = self.request.query_params.get('name')
        active = self.request.query_params.get('active')
        user = self.request.query_params.get('user')
        dev_only = self.request.query_params.get('dev_only')
        
        if active is not None:
            queryset = queryset.filter(active=active)
        if name is not None:
            queryset = queryset.filter(status=name)
        if user is not None:
            queryset = queryset.filter(user=user)
        if dev_only is not None:
            queryset = queryset.filter(dev_only=dev_only)
        return queryset
    
class SalonNameExtendViewSet(viewsets.ModelViewSet):
    # queryset = SalonName.objects.all()
    serializer_class = SalonNameExtendSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','user','url_slug','gstin','dev_only','active']
    def get_queryset(self):
        queryset = SalonName.objects.all()
        name = self.request.query_params.get('name')
        active = self.request.query_params.get('active')
        user = self.request.query_params.get('user')
        dev_only = self.request.query_params.get('dev_only')
        
        if active is not None:
            queryset = queryset.filter(active=active)
        if name is not None:
            queryset = queryset.filter(status=name)
        if user is not None:
            queryset = queryset.filter(user=user)
        if dev_only is not None:
            queryset = queryset.filter(dev_only=dev_only)
        return queryset

class SalonOwnerRightsViewSet(viewsets.ModelViewSet):
    queryset = SalonOwnerRights.objects.all()
    serializer_class = SalonOwnerRightsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class SalonStaffRightsViewSet(viewsets.ModelViewSet):
    queryset = SalonStaffRights.objects.all()
    serializer_class = SalonStaffRightsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class SalaryAndCommissionViewSet(viewsets.ModelViewSet):
    queryset = SalaryAndCommission.objects.all()
    serializer_class = SalaryAndCommissionSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class ServiceHistoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class MembershipServicesViewSet(viewsets.ModelViewSet):
    queryset = MembershipServices.objects.all()
    serializer_class = MembershipServicesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class LoyaltyPointMasterViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyPointMaster.objects.all()
    serializer_class = LoyaltyPointMasterSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class UnitTypeViewSet(viewsets.ModelViewSet):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class DeadStockViewSet(viewsets.ModelViewSet):
    queryset = DeadStock.objects.all()
    serializer_class = DeadStockSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class InHouseProductUseViewSet(viewsets.ModelViewSet):
    queryset = InHouseProductUse.objects.all()
    serializer_class = InHouseProductUseSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class StockHistoryViewSet(viewsets.ModelViewSet):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class OffersViewSet(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class GiftCardViewSet(viewsets.ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class AppointmentViewSet(viewsets.ModelViewSet):
    # queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        customer = self.request.query_params.get('customer')
        active = self.request.query_params.get('active')
        services = self.request.query_params.get('services')
        salon = self.request.query_params.get('salon')
        
        if active is not None:
            queryset = queryset.filter(active=active)
        if customer is not None:
            queryset = queryset.filter(customer=customer)
        if services is not None:
            queryset = queryset.filter(services=services)
        if salon is not None:
            queryset = queryset.filter(salon=salon)
        return queryset
    
class AppointmentExtendViewSet(viewsets.ModelViewSet):
    # queryset = Appointment.objects.all()
    serializer_class = AppointmentExtendSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        customer = self.request.query_params.get('customer')
        active = self.request.query_params.get('active')
        services = self.request.query_params.get('services')
        salon = self.request.query_params.get('salon')
        
        if active is not None:
            queryset = queryset.filter(active=active)
        if customer is not None:
            queryset = queryset.filter(customer=customer)
        if services is not None:
            queryset = queryset.filter(services=services)
        if salon is not None:
            queryset = queryset.filter(salon=salon)
        return queryset

class ChairViewSet(viewsets.ModelViewSet):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class TargetHistoryViewSet(viewsets.ModelViewSet):
    queryset = TargetHistory.objects.all()
    serializer_class = TargetHistorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class CustomerHistoryViewSet(viewsets.ModelViewSet):
    queryset = CustomerHistory.objects.all()
    serializer_class = CustomerHistorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

class SalonStaffViewSet(viewsets.ModelViewSet):
    # queryset = SalonStaff.objects.all()
    serializer_class = SalonStaffSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

    def get_queryset(self):
        queryset = SalonStaff.objects.all()
        status = self.request.query_params.get('status')
        active = self.request.query_params.get('active')
        user = self.request.query_params.get('user')
        salon = self.request.query_params.get('salon')
        dev_only = self.request.query_params.get('dev_only')
        # queryset.timeout = 60*60
        if active is not None:
            queryset = queryset.filter(active=active)
        if status is not None:
            queryset = queryset.filter(status=status)
        if user is not None:
            queryset = queryset.filter(user=user)
        if salon is not None:
            queryset = queryset.filter(salon=salon)
        if dev_only is not None:
            queryset = queryset.filter(dev_only=dev_only)
        return queryset
    
class SalonStaffExtendViewSet(viewsets.ModelViewSet):
    # queryset = SalonStaff.objects.all()
    serializer_class = SalonStaffExtendSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

    def get_queryset(self):
        queryset = SalonStaff.objects.all()
        status = self.request.query_params.get('status')
        active = self.request.query_params.get('active')
        user = self.request.query_params.get('user')
        salon = self.request.query_params.get('salon')
        dev_only = self.request.query_params.get('dev_only')
        # queryset.timeout = 60*60
        if active is not None:
            queryset = queryset.filter(active=active)
        if status is not None:
            queryset = queryset.filter(status=status)
        if user is not None:
            queryset = queryset.filter(user=user)
        if salon is not None:
            queryset = queryset.filter(salon=salon)
        if dev_only is not None:
            queryset = queryset.filter(dev_only=dev_only)
        return queryset
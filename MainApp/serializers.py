from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import *

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self,instance, validated_data):

        if validated_data.get('password') == instance.password or validated_data.get('password') == None:
            return super(UserSerializer, self).update(instance,validated_data)
        else:
            validated_data['password'] = make_password(validated_data.get('password', instance.password))
            return super(UserSerializer, self).update(instance,validated_data)
    
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is not active"
                    raise exceptions.ValidationError(msg)
            else:
                try:
                    check = User.objects.get(email=email)
                    # print(check.password)
                    msg = "Password is incorrect for {}".format(check.email)
                    raise exceptions.ValidationError(msg)
                except User.DoesNotExist:
                    msg = "This email not registered with us"
                    raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.ValidationError(msg)
        return data
    
class IncorporationImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncorporationImages
        fields = '__all__'

class OtherImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherImages
        fields = '__all__'

class SalonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonName
        fields = '__all__'

class SalonNameExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonName
        fields = '__all__'
        depth = 1

class SalonOwnerRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonOwnerRights
        fields = '__all__'

class SalonStaffRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonStaffRights
        fields = '__all__'

class SalaryAndCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryAndCommission
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = '__all__'

class MembershipServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipServices
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LoyaltyPointMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyPointMaster
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class DeadStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadStock
        fields = '__all__'

class InHouseProductUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InHouseProductUse
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = '__all__'

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        depth = 1

class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'

class TargetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetHistory
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class CustomerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerHistory
        fields = '__all__'

class SalonStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonStaff
        fields = '__all__'

class SalonStaffExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonStaff
        fields = '__all__'
        depth = 1
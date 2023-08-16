from django.db import models
from django.core.validators import (FileExtensionValidator, MinValueValidator, MaxValueValidator)
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.core.exceptions import ValidationError
import datetime
from SalonManagmentSystem.utils import (ID_TYPES,Attendance_STATUS,marital_status,discount_type,transaction_type,targer_type,
                                        appointment_status,user_STATUS)

class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True,blank=True, null=True)
    mobile = models.CharField(max_length=10,blank=True, null=True)
    alternate_mobile = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    referral_code = models.CharField(max_length=250, blank=True, null=True)
    referral_user = models.ManyToManyField('self', blank=True,symmetrical=False)
    staff = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)

    address_line_1 = models.CharField(max_length=120, null=True, blank=True, help_text="User Address two")
    address_line_2 = models.CharField(max_length=120, null=True, blank=True, help_text="User Address two")
    locality = models.CharField(max_length=30, null=True, blank=True, help_text="User Locality")
    district = models.CharField(max_length=50, null=True, blank=True, help_text="User District")
    area_name = models.CharField(max_length=60, null=True, blank=True, help_text="User Area Name")
    city_name = models.CharField(max_length=35, null=True, blank=True, help_text="User City Name")
    country = models.CharField(max_length=30, default='INDIA')
    state = models.CharField(max_length=30, help_text="User State Name", null=True, blank=True,)
    postal_code = models.PositiveIntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)],null=True, blank=True)

    referral_used = models.BooleanField(default=False)
    dob = models.DateTimeField(null=True, blank=True)

    bank_account_no = models.CharField(max_length=18, null=True, blank=True, help_text="User bank account no")
    bank_account_type = models.CharField(max_length=18, null=True, blank=True, help_text="User bank type")
    bank_branch_name = models.CharField(max_length=18, null=True, blank=True, help_text="User bank type")
    bank_ifsc_code = models.CharField(max_length=15, null=True, blank=True, help_text="User bank IFSC")
    vpa_upi = models.CharField(max_length=50, null=True, blank=True, help_text="User VPA or UPI")

    id_proof_type = models.CharField(max_length=20, choices=ID_TYPES, null=True, blank=True,
                                     help_text="Please select id proof type carefully, we will verify your identity")
    id_proof = models.FileField(upload_to='images/ids/',
                                help_text='Only png,jpeg,jpg images are allowed, max 2MB size', null=True, blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserManager()

    def __str__(self):
        return self.email

class IncorporationImages(models.Model):
    images = models.ImageField(upload_to='images/incorporation/', help_text='Only png,jpeg,jpg images are allowed',
                                       null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'webp'])])
            
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.images)
    
class OtherImages(models.Model):
    images = models.ImageField(upload_to='images/other/', help_text='Only png,jpeg,jpg images are allowed',
                                       null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'webp'])])
            
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.images)

class SalonName(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True,help_text="Salon name")
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    url_slug = models.CharField(max_length=225,null=True, blank=True,help_text="Salon url_slug")
    address_line_1 = models.CharField(max_length=120, help_text="Salon Address two")
    address_line_2 = models.CharField(max_length=120, null=True, blank=True, help_text="Salon Address two")
    locality = models.CharField(max_length=30, null=True, blank=True, help_text="Salon Locality")
    district = models.CharField(max_length=50, null=True, blank=True, help_text="Salon District")
    area_name = models.CharField(max_length=60, null=True, blank=True, help_text="Salon Area Name")
    city_name = models.CharField(max_length=35, null=True, blank=True, help_text="Salon City Name")
    country = models.CharField(max_length=30, default='INDIA')
    state = models.CharField(max_length=30, help_text="Salon State Name")
    latitude = models.CharField(max_length=15, null=True, blank=True, help_text="Salon latitude")
    longitude = models.CharField(max_length=15, null=True, blank=True, help_text="Salon longitude")
    gstin = models.CharField(max_length=20, null=True, blank=True, help_text="Salon GSTIN number")
    pan_card_number = models.CharField(max_length=20, null=True, blank=True, help_text="Salon PAN CARD number")
    incorporation_number = models.CharField(max_length=20, null=True, blank=True, help_text="Salon PAN CARD number")
    other_number = models.CharField(max_length=20, null=True, blank=True, help_text="Salon PAN CARD number")
    bill_name = models.CharField(max_length=20, null=True, blank=True, help_text="Salon GSTIN number")
    bank_account_no = models.CharField(max_length=18, null=True, blank=True, help_text="Salon bank account no")
    bank_account_type = models.CharField(max_length=18, null=True, blank=True, help_text="Salon bank type")
    bank_branch_name = models.CharField(max_length=18, null=True, blank=True, help_text="Salon bank type")
    bank_ifsc_code = models.CharField(max_length=15, null=True, blank=True, help_text="Salon bank IFSC")
    vpa_upi = models.CharField(max_length=50, null=True, blank=True, help_text="Salon VPA or UPI")
    
    salon_logo_500x500 = models.ImageField(upload_to='images/logo/',
                                help_text='Kindly upload 500x500 px image or square shaped images in png, jpeg, jpg format',
                                null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    salon_logo_250x250 = models.ImageField(upload_to='images/logo/',
                                null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    salon_logo_128x128 = models.ImageField(upload_to='images/logo/',
                                null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    pan_card = models.ImageField(upload_to='images/pan_card/', help_text='Only png,jpeg,jpg images are allowed',
                                null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    gstin_image = models.ImageField(upload_to='images/gstin/', help_text='Only png,jpeg,jpg images are allowed',
                                       null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    
    incorporation_images = models.ManyToManyField(IncorporationImages, blank=True)
    other_images = models.ManyToManyField(OtherImages, blank=True)
    
    chain = models.PositiveIntegerField(default=1)
    postal_code = models.PositiveIntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    
    active = models.BooleanField(default=False)
    dev_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print("Salon logo", self.salon_logo_500x500)
        if self.salon_logo_500x500:

            from PIL import Image
            from django.core.files import File
            from io import BytesIO
            
            main_img = self.salon_logo_500x500
            
            if "/" in main_img.name:
                original_name = main_img.name.split("/")
                original_name = original_name[-1]
                image_name = str(original_name).split(".")
                main_image = Image.open(self.salon_logo_500x500.url.lstrip("/"))
                
                image_extension = image_name[1]
                image_format = "png" if image_extension == "png" else "jpeg"
                image_name = image_name[0]  
            else:
                image_name = str(self.salon_logo_500x500).split(".")
                main_image = Image.open(self.salon_logo_500x500)
                
                image_extension = image_name[1]
                image_format = "png" if image_extension == "png" else "jpeg"
                image_name = image_name[0]    
    
                io_ob2 = BytesIO()
                image2 = main_image
                image2 = image2.resize((250, 250))
                image2.save(io_ob2, format=image_format)
                image_name2 = image_name + "_250." + image_extension
                self.salon_logo_250x250 = File(io_ob2, image_name2)
        
                io_ob3 = BytesIO()
                image3 = main_image
                image3 = image3.resize((128, 128))
                image3.save(io_ob3, format=image_format)
                image_name3 = image_name + "_128." + image_extension
                self.salon_logo_128x128 = File(io_ob3, image_name3)
    
        else:
            self.salon_logo_128x128 = None
            self.salon_logo_250x250 = None
        super(SalonName, self).save(*args, **kwargs)

class SalonStaff(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=120, choices=user_STATUS, default="Pending")
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=30, null=True, blank=True, help_text="Staff Role")
    
    active = models.BooleanField(default=False)
    dev_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class SalonOwnerRights(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
    active = models.BooleanField(default=False)
    dev_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class SalonStaffRights(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    active = models.BooleanField(default=False)
    dev_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class SalaryAndCommission(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)

    salary = models.PositiveIntegerField(default=1)
    commission = models.PositiveIntegerField(default=1)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Attendance(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.datetime.now)
    day = models.CharField(max_length=225,null=True, blank=True)
    starting_time = models.DateTimeField(auto_now=True)
    endinging_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=120, choices=Attendance_STATUS, default="Present")

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Services(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=225,null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)

    gstin = models.CharField(max_length=20, null=True, blank=True)
    hsn = models.CharField(max_length=20, null=True, blank=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ServiceHistory(models.Model):
    services = models.ForeignKey(Services, null=True, blank=True, on_delete=models.DO_NOTHING)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class MembershipServices(models.Model):
    discount = models.PositiveIntegerField(null=True, blank=True)
    free_visits = models.PositiveIntegerField(null=True, blank=True)

    service_id = models.ManyToManyField(Services, blank=True)
    salon = models.ForeignKey(SalonName, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class Membership(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    type = models.CharField(max_length=225,null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)
    discount_type = models.CharField(max_length=120, choices=discount_type, default="Flat")

    membership_service_id = models.ManyToManyField(MembershipServices, blank=True)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)

    starting_time = models.DateTimeField(auto_now=True)
    endinging_time = models.DateTimeField(null=True, blank=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.CharField(max_length=120, choices=marital_status, default="Single")
    dob = models.DateTimeField(null=True, blank=True)
    doa = models.DateTimeField(null=True, blank=True)
    loyalty_point = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=255, unique=True,blank=True, null=True)
    mobile = models.CharField(max_length=10,blank=True, null=True)
    referred_by = models.CharField(max_length=10,blank=True, null=True)

    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    membership_id = models.ForeignKey(Membership, null=True, blank=True, on_delete=models.DO_NOTHING)

    last_visited = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class LoyaltyPointMaster(models.Model):
    transaction_type = models.CharField(max_length=120, null=True, blank=True, choices=transaction_type, default="Debit")
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
    
class Category(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Brand(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class UnitType(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    short_name = models.CharField(max_length=225,null=True, blank=True)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Products(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=225,null=True, blank=True)
    gstin = models.CharField(max_length=20, null=True, blank=True)
    hsn = models.CharField(max_length=20, null=True, blank=True)

    mrp = models.PositiveIntegerField(default=0)
    discount_mrp = models.PositiveIntegerField(default=0)
    purchase_mrp = models.PositiveIntegerField(default=0)
    margin_on_purchase_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    item_size = models.PositiveIntegerField(default=0)

    image = models.FileField(upload_to='images/product_name/',
                                help_text='Only png,jpeg,jpg images are allowed, max 2MB size', null=True, blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])


    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    unit_type = models.ForeignKey(UnitType, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Stock(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)
    quality = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class DeadStock(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)
    quality = models.PositiveIntegerField(default=0)
    purchase_price = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class InHouseProductUse(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)
    purchase_price = models.PositiveIntegerField(default=0)
    quality = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    used_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class Sales(models.Model):
    quality = models.PositiveIntegerField(default=0)
    discount_flat = models.PositiveIntegerField(default=0)
    discount_percentage = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)

    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="Staff")
    sold_to_staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="Sold_to_Staff")

    used_date = models.DateTimeField(auto_now_add=True)
    sales_id = models.CharField(max_length=225,null=True, blank=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class Purchase(models.Model):
    vendor = models.CharField(max_length=225,null=True, blank=True)
    document_type = models.CharField(max_length=225,null=True, blank=True)
    bill_number = models.CharField(max_length=225,null=True, blank=True)

    mrp = models.PositiveIntegerField(default=0)
    purchase_price = models.PositiveIntegerField(default=0)
    discount_flat = models.PositiveIntegerField(default=0)
    discount_percentage = models.PositiveIntegerField(default=0)

    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)

    purchase_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images/purchase/',
                                help_text='Only png,jpeg,jpg images are allowed, max 2MB size', null=True, blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class StockHistory(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.DO_NOTHING)
    sales = models.ForeignKey(Sales, null=True, blank=True, on_delete=models.DO_NOTHING)
    stock = models.ForeignKey(Stock, null=True, blank=True, on_delete=models.DO_NOTHING)
    purchase = models.ForeignKey(Purchase, null=True, blank=True, on_delete=models.DO_NOTHING)
    in_house_product_use = models.ForeignKey(InHouseProductUse, null=True, blank=True, on_delete=models.DO_NOTHING)
    dead_stock = models.ForeignKey(DeadStock, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stock)

class Offers(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services, blank=True,symmetrical=False)
    name = models.CharField(max_length=225,null=True, blank=True)
    offer_code = models.CharField(max_length=225,null=True, blank=True)
    uses_per_customer = models.PositiveIntegerField(default=1)
    min_order_amount = models.IntegerField(help_text="Minimum this much of billing amount is required inrder to avail discount", null=True, blank=True)
    discount_type = models.CharField(choices=(
        ("percent", "Percent"),
        ("flat", "Flat Discount"),
        ("Cashback", "Cashback")
    ), null=True, blank=True, help_text="Percent means x% of amount will be discounted. Flat discount means x amount will be reduced from the billing amount", max_length=30)
    flat_discount_amount = models.IntegerField(help_text="Amount for how much will the discount be given?", null=True, blank=True)
    percent_discount = models.IntegerField(help_text="What percent of discount on amount shall be given?", null=True, blank=True)
    percent_discount_max_limit = models.IntegerField(help_text="Till what amount the discount will be given?", null=True, blank=True)
    cashback_amount = models.IntegerField(help_text="Give cashback in their wallet", null=True, blank=True)
    
    visible_on_app = models.BooleanField(default=True, help_text="If this is checked only, the offer will be visible on the website/app")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.offer_code)
    
class GiftCard(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    gift_card_code = models.CharField(max_length=225,null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.gift_card_code)
    
class Expense(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=225,null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    dob = models.DateTimeField(null=True, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class Appointment(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.DO_NOTHING)
    services = models.ForeignKey(Services, null=True, blank=True, on_delete=models.DO_NOTHING)

    booking_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                   help_text='Time should be in 18:12:00 this format')
    booking_date = models.DateField(blank=True, null=True)

    appointment_status = models.CharField(max_length=120, choices=appointment_status, default="Booked")

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class Chair(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    services = models.ForeignKey(Services, null=True, blank=True, on_delete=models.DO_NOTHING)

    chair_number = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class Target(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey(User,null=True, blank=True, on_delete=models.DO_NOTHING)

    daily_target = models.PositiveIntegerField(default=0)
    monthly_target = models.PositiveIntegerField(default=0)
    yearly_target = models.PositiveIntegerField(default=0)

    appointment_status = models.CharField(max_length=120, choices=appointment_status, default="Sales")

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)
    
class TargetHistory(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey(User,null=True, blank=True, on_delete=models.DO_NOTHING)
    services = models.ForeignKey(Services, null=True, blank=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)

    achieved_amount = models.PositiveIntegerField(default=0)
    not_achieved_amount = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.salon)

class Bill(models.Model):
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    gift_cart = models.ForeignKey(GiftCard, null=True, blank=True, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offers, null=True, blank=True, on_delete=models.CASCADE)
    chair_id = models.ForeignKey(Chair, null=True, blank=True, on_delete=models.CASCADE)
    membership_id = models.ForeignKey(Membership, null=True, blank=True, on_delete=models.CASCADE)
    loyalty_id = models.ForeignKey(LoyaltyPointMaster, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, blank=True, on_delete=models.DO_NOTHING)

    bill_number = models.CharField(max_length=225,null=True, blank=True)

    date = models.DateTimeField(default=datetime.datetime.now)
    gstin = models.CharField(max_length=20, null=True, blank=True, help_text="Salon GSTIN number")

    discount_flat = models.PositiveIntegerField(default=0)
    discount_percentage = models.PositiveIntegerField(default=0)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bill_number)
    
class CustomerHistory(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.DO_NOTHING)
    salon = models.ForeignKey(SalonName, null=True, blank=True, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, null=True, blank=True, on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.datetime.now)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer)
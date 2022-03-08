from django.db import models


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    restaurant_type = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class RestaurantBranch(models.Model):
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE, related_name='restaurant_branch')
    branch_name = models.CharField(max_length=50)
    branch_manager = models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)


class Owner(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Stadium(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner', null=False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)


class StadiumAvailabililty(models.Model):
    stadium_id = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='stadium', null=False)
    free_slots_start_time = models.DateTimeField(auto_now=True)
    free_slots_end_time = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)


class Reservation(models.Model):
    stadium_id = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='stadium_reserv', null=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer', null=False)
    reserved_slot = models.ForeignKey(StadiumAvailabililty, on_delete=models.CASCADE, related_name='stadium_availability', null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)
















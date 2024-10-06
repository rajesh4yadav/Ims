from rest_framework.serializers import ModelSerializer
from .models import ProductType,Product,User
from django.contrib.auth.models import Group





class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
        

class UserSerializer(ModelSerializer):
    class Meta:
        model =  User
        fields =  ['full_name','email','password','image','phone_number','groups']


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields =  '__all__'

        
    
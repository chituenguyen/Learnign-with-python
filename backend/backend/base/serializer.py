from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('_get_name')
    _id = serializers.SerializerMethodField('_get_id')
    is_Admin = serializers.SerializerMethodField('_get_isAdmin')

    def _get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def _get_isAdmin(self, obj):
        return obj.is_staff

    def _get_id(self, obj):
        return obj.id

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'is_Admin', '_id']
    ### customize serializer

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'is_Admin', '_id','token']

    def get_token(self, obj): #refresh token ???
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ShippingAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAdress
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)


    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self,obj):
        items=obj.orderitem_set.all()
        serializer=OrderItemSerializer(items,many=True)
        return serializer.data

    def get_shippingAddress(self,obj):
        try:
            address=ShippingAdressSerializer(obj.shippingadress,many=False).data
        except:
            address=False
        return address

    def get_user(self,obj):
        user=obj.user
        serializer=UserSerializer(user,many=False)
        return serializer.data
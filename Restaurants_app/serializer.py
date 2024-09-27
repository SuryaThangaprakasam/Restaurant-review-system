from rest_framework import serializers
from Restaurants_app.models import Restaurant,Menu,User,Review,Reservation

class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    cuisine_type = serializers.CharField(max_length=100)
    average_rating = serializers.FloatField(default=0)

    class Meta:
        fields = ['id','name','address','cuisine_type','average_rating']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance

class MenuSerializer(serializers.ModelSerializer):

    dishName_len = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id','restaurant','dish_name','price','description','dishName_len']

    def get_dishName_len(self,obj):
        return len(obj.dish_name)

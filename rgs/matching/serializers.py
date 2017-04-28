from rest_framework import serializers
from models import RGSUser, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = (
            'desc',
        )

class RGSUserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True)
	
    class Meta:
        model = RGSUser
        fields = (
            'name',
        	'lastname',
        	'gender',
        	'age',
        	'interests'
        )
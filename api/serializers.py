from attr import field
from rest_framework import serializers
from .models import Borrower, Stateloan


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields= '__all__'

class StateloanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stateloan
        fields= '__all__'


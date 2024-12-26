from rest_framework import serializers 
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta :
        model = Member
        fields = ['id', 'name', 'email', 'birth', 'join_date']
from .models import Member
from django.shortcuts import render, redirect
#from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemberSerializer

# 회원 전체 목록 조회
@api_view(['GET'])
def member_list(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

# 회원 가입
@api_view(['POST'])
def member_create(request):
    serializer = MemberSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)
   

@api_view(['GET','PUT','DELETE'])
def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)

    if request.method == 'GET': # 회원 상세 조회
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    
    elif request.method == 'PUT': # 회원 정보 수정
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    
    elif request.method == 'DELETE': #회원 삭제
        member.delete()
        return Response(status=200)


@api_view(['PUT'])
def member_update(request, member_id):
    member = Member.objects.get(id=member_id)
    

    



    
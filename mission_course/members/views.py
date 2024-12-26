from .models import Member
#from django.shortcuts import render, redirect
#from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemberSerializer
from .serializers import MemberListSerializer

# 회원 전체 목록 조회
@api_view(['GET'])
def member_list(request):
    members = Member.objects.all()
    serializer = MemberListSerializer(members, many=True)
    return Response(serializer.data)

# 회원 가입
@api_view(['POST'])
def member_create(request):
    serializer = MemberSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data" : serializer.data, "message" : "가입되었습니다."}, status=200)
    return Response(serializer.errors, status=400)
   

@api_view(['GET','PUT','DELETE'])
def member_detail(request, member_id):
    try:
        member = Member.objects.get(id=member_id)
    except Member.DoesNotExist:
        return Response({"message" : "존재하지 않는 사용자입니다."}, status=404)

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
        return Response({"message" : "삭제되었습니다." }, status=200)



    



    
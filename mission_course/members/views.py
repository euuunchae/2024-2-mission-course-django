from django.shortcuts import render
from members.models import Member

# Create your views here.
def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    context = {'member' : member}
    return render(request, 'question_detail.html', context)

def member_list(request):
    members = Member.objects.all()
    context = {'members' : members}
    return render(request, 'member_list.html', context)


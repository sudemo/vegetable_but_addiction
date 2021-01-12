from django.contrib.auth.models import User,Group
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets,views
from .models import Capsules
from cup.serializer import CapsulesSerializer,UserSerializer,GroupSerializer

from django.http import HttpResponse


def get_ip(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        print(ip)
    else:
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
    return HttpResponse("你的IP是"+ip)


def index():
    return HttpResponse('你来到了一片荒地')


class CapsuleViewSet(viewsets.ModelViewSet):
    queryset = Capsules.objects.all().order_by('id')  # create_time
    serializer_class = CapsulesSerializer
# @csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# @csrf_exempt
class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

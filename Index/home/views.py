# coding : utf8
from django.shortcuts import render
from django.http.response import HttpResponse

# 首页
def index(request):
    return render(request, 'Index/index.html')
# 发帖页
def posted(request):
     return render(request, 'Index/posted.html')
# 帖子详情页
def posted_detils(request):

    return render(request, 'Index/posted_details.html')
# 登录页
def sigin(request):
    return HttpResponse('1')
# 用户信息页
def user_info(request):
    return HttpResponse('1')
# 用户信息设置页
def user_settings(request):
    return HttpResponse('1')
# 用户注册页
def sigup(request):
    return HttpResponse('1')
# 消息通知页
def message(request):
    return HttpResponse('1')



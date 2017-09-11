# coding : utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# 首页
def index(request, pid = None):

    enum1 = models.TopClassifyEnum.objects.filter(level = 0)
    pid = int(pid)
    enum2 = None
    if pid: 
        enum2 = models.TopClassifyEnum.objects.filter(pid = pid)
        list_id = [id.id for id in enum2]
        # 获取相关帖子信息
        if list_id:
            list_data = models.PostedProbady.select_full_data(*list_id)
        else:
            list_data = []
    else:
        list_data = models.PostedProbady.select_full_data()
    # 分页用js插件做
  
        
    return render(request, 'Index/index.html', {'enum1':enum1, 'enum2':enum2, 'list_data':list_data})
#'''————————————————————————————————————————————————————————————————'''
# 发帖页
def posted(request):
     return render(request, 'Index/posted.html')
# 帖子详情页
def posted_detils(request):

    return render(request, 'Index/posted_details.html')
# 登录页
def sigin(request):
    return render(request, 'Index/sigin.html')
# 用户信息页
def user_info(request):
    return HttpResponse('1')
# 用户信息设置页
def user_settings(request):
    return HttpResponse('1')
# 用户注册页
def sigup(request):
     return render(request, 'Index/sigup.html')
# 消息通知页
def message(request):
    return HttpResponse('1')



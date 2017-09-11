# coding : utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# ��ҳ
def index(request, pid = None):

    enum1 = models.TopClassifyEnum.objects.filter(level = 0)
    pid = int(pid)
    enum2 = None
    if pid: 
        enum2 = models.TopClassifyEnum.objects.filter(pid = pid)
        list_id = [id.id for id in enum2]
        # ��ȡ���������Ϣ
        if list_id:
            list_data = models.PostedProbady.select_full_data(*list_id)
        else:
            list_data = []
    else:
        list_data = models.PostedProbady.select_full_data()
    # ��ҳ��js�����
  
        
    return render(request, 'Index/index.html', {'enum1':enum1, 'enum2':enum2, 'list_data':list_data})
#'''��������������������������������������������������������������������������������������������������������������������������������'''
# ����ҳ
def posted(request):
     return render(request, 'Index/posted.html')
# ��������ҳ
def posted_detils(request):

    return render(request, 'Index/posted_details.html')
# ��¼ҳ
def sigin(request):
    return render(request, 'Index/sigin.html')
# �û���Ϣҳ
def user_info(request):
    return HttpResponse('1')
# �û���Ϣ����ҳ
def user_settings(request):
    return HttpResponse('1')
# �û�ע��ҳ
def sigup(request):
     return render(request, 'Index/sigup.html')
# ��Ϣ֪ͨҳ
def message(request):
    return HttpResponse('1')



# coding : utf8
from django.shortcuts import render
from django.http.response import HttpResponse

# ��ҳ
def index(request):
    return render(request, 'Index/index.html')
# ����ҳ
def posted(request):
     return render(request, 'Index/posted.html')
# ��������ҳ
def posted_detils(request):

    return render(request, 'Index/posted_details.html')
# ��¼ҳ
def sigin(request):
    return HttpResponse('1')
# �û���Ϣҳ
def user_info(request):
    return HttpResponse('1')
# �û���Ϣ����ҳ
def user_settings(request):
    return HttpResponse('1')
# �û�ע��ҳ
def sigup(request):
    return HttpResponse('1')
# ��Ϣ֪ͨҳ
def message(request):
    return HttpResponse('1')



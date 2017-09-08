from django.db import models

# coding:utf-8
'''�����������������������������������޷���˵�ѡ���������������������������������������'''
import time
class TopClassifyEnum(models.Model):
    enumName = models.CharField(max_length=50)
    pid = models.IntegerField()
    leveval = models.IntegerField()
    
'''�������������������������������������б���������������������������������������'''  
class PostedProbady(models.Model):
    '''������id������ʱ�䣬���ӱ��⣬�������ݣ����ӵ�������ղ�����������������������������������������'''
    uid = models.IntegerField()
    ctime = models.IntegerField(default = time.time())
    title = models.CharField(max_length=50)
    content = models.TextField()
    clickNum = models.IntegerField(db_index = True)
    voltNums = models.IntegerField()
    belittleNums = models.IntegerField()
    commentNums = models.IntegerField(db_index = True)
    classify = models.IntegerField(db_index = True)
    
'''�������������������������������������������������������������������������������'''
class PostedReply(models.Model):
    '''����id���ظ���id���ظ��ظ���id��Ĭ����0,0��ֱ�ӻظ����ӡ��������������������ظ�ʱ��,�ظ�����'''
    postedId = models.IntegerField()
    uId = models.IntegerField()
    replyId = models.IntegerField(default = 0)
    voltNums = models.IntegerField()
    belittleNums = models.IntegerField()
    ctime = models.IntegerField(default = time.time())
    content = models.TextField()
    
'''��������������������������������ǰ̨�û�������Ϣ����������������������������������������''' 
class User(models.Model):
    '''�û��������룬���䣬����ʱ�䣬����¼ʱ�䣬�Ƿ������¼'''
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email  = models.CharField()
    ctime = models.IntegerField(default = time.time())
    lastSiginTime = models.IntegerField(default = time.time())
    allowLog = models.BooleanField(default = True)
    
'''��������������������������������ǰ̨�û���ϸ��Ϣ����������������������������������������''' 
class UserDetail(models.Model):
    '''�û�id,Ĭ��ͷ�񣬸���ǩ��'''
    pass
'''��������������������������������ǰ̨�û����ġ���������������������������������������''' 
    

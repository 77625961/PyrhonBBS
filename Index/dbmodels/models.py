from django.db import models

# coding:utf-8
'''————————————————无限分类菜单选项————————————————————'''
import time
class TopClassifyEnum(models.Model):
    enumName = models.CharField(max_length=50)
    pid = models.IntegerField()
    leveval = models.IntegerField()
    
'''————————————————帖子列表————————————————————'''  
class PostedProbady(models.Model):
    '''发帖人id，发帖时间，帖子标题，帖子内容，帖子点击数，收藏数，点赞数，拉黑数，帖子评论数，所属分类'''
    uid = models.IntegerField()
    ctime = models.IntegerField(default = time.time())
    title = models.CharField(max_length=50)
    content = models.TextField()
    clickNum = models.IntegerField(db_index = True)
    voltNums = models.IntegerField()
    belittleNums = models.IntegerField()
    commentNums = models.IntegerField(db_index = True)
    classify = models.IntegerField(db_index = True)
    
'''————————————————帖子详情表————————————————————'''
class PostedReply(models.Model):
    '''帖子id，回复人id，回复回复的id【默认是0,0是直接回复帖子】，点赞数，拉黑数，回复时间,回复内容'''
    postedId = models.IntegerField()
    uId = models.IntegerField()
    replyId = models.IntegerField(default = 0)
    voltNums = models.IntegerField()
    belittleNums = models.IntegerField()
    ctime = models.IntegerField(default = time.time())
    content = models.TextField()
    
'''————————————————前台用户基本信息————————————————————''' 
class User(models.Model):
    '''用户名，密码，邮箱，创建时间，最后登录时间，是否允许登录'''
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email  = models.CharField()
    ctime = models.IntegerField(default = time.time())
    lastSiginTime = models.IntegerField(default = time.time())
    allowLog = models.BooleanField(default = True)
    
'''————————————————前台用户详细信息————————————————————''' 
class UserDetail(models.Model):
    '''用户id,默认头像，个性签名'''
    pass
'''————————————————前台用户中心————————————————————''' 
    

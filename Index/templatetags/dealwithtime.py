#-*- coding:utf-8 -*-
from django import template
import time

register = template.Library() # 实例化模板


# 格式时间过滤器
@register.filter # 过滤器注册
def dealwithtime(y):
    diff = time.time() - y
    if diff > 3600:
        return '{} 小时前'.format(int(diff / 3600))
    if diff > 60:
        return '{} 分钟前'.format(int(diff / 60))
    return '{} 秒前'.format(int(diff))
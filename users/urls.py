# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.urls import path

from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView

app_name = 'users'    #django2.0需要加上，否则报错
urlpatterns = [
    #用户信息
    path('info/', UserinfoView.as_view(), name="user_info"),

    #用户头像上传
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),

    #用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),

    #发送邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),

    #修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),

    #我的课程
    path('mycourse/', MyCourseView.as_view(), name="mycourse"),

    #我收藏的课程机构
    path('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),

    #我收藏的授课讲师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),

    #我收藏的课程
    path('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),

    #我的消息
    path('mymessage/', MymessageView.as_view(), name="mymessage"),
]
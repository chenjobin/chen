# -*- coding: utf-8 -*-

from django.urls import path, include

from .views import OrgView,OrgHomeView,AddUserAskView,AddFavView,OrgCourseView,OrgDescView,OrgTeacherView
from .views import TeacherListView, TeacherDetailView

app_name = 'organization'    #django2.0需要加上，否则报错
urlpatterns = [
    #课程机构列表页
    path(r'list/', OrgView.as_view(), name="org_list"),
    path(r'add_ask/', AddUserAskView.as_view(), name="add_ask"),
    path(r'home/<int:org_id>/', OrgHomeView.as_view(), name="org_home"),
    path(r'course/<int:org_id>/', OrgCourseView.as_view(), name="org_course"),
    path(r'desc/<int:org_id>/', OrgDescView.as_view(), name="org_desc"),
    path(r'org_teacher/<int:org_id>/', OrgTeacherView.as_view(), name="org_teacher"),
    #
    #机构收藏
    path(r'add_fav/', AddFavView.as_view(), name="add_fav"),
    #
    #讲师列表页
    path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),

    #讲师详情页
    path('teacher/detail/<int:teacher_id>/', TeacherDetailView.as_view(), name="teacher_detail"),
]
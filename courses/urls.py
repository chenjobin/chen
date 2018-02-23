# -*- coding: utf-8 -*-

from django.urls import path

from .views import CourseDetailView #CourseInfoView, CommentsView, AddComentsView

app_name = 'courses'    #django2.0需要加上，否则报错
urlpatterns = [
    #课程列表页
    # url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    path('detail/<int:course_id>/', CourseDetailView.as_view(), name="course_detail"),

    # url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    #课程评论
    # url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    #添加课程评论
    # url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

]

"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
from django.views.static import serve

import xadmin
from users.views import IndexView
from users.views import LoginView,LogoutView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from mooc.settings import MEDIA_ROOT,STATIC_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    path(r'active/<slug:active_code>/', ActiveUserView.as_view(), name="user_active"),
    path(r'forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    path(r'reset/<slug:active_code>/', ResetView.as_view(), name="reset_pwd"),
    path(r'modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构url配置
    path(r'org/', include('organization.urls', namespace="org")),
    # 课程相关url配置
    path('course/', include('courses.urls', namespace="course")),
    # 配置上传文件的访问处理函数
    path('media/<path:path>', serve, {"document_root": MEDIA_ROOT}),   #str path int slug uuid五种

    path('static/<path:path>',  serve, {"document_root":STATIC_ROOT}),

    # 课程相关url配置
    path('users/', include('users.urls', namespace="users")),

    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
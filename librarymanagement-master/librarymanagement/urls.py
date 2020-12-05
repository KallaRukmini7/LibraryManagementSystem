"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView;



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),

    path('contactus', views.contactus_view),
    path('aboutus', views.aboutus_view),




    path('reset_password/',PasswordResetView.as_view(template_name='registration/password_reset.html'),name="reset_password"),
    path('reset_password_sent/',PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html') ,name="password_reset_confirm"),
    path('reset_password_completed/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name="password_reset_complete"),


]

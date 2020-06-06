from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views # import za PasswordReset
from . import views





urlpatterns = [
    path('pozdrav/<str:pk>/', views.ime, name="pozdrav"),
    path('', views.home, name="home"),

    path('profile/edit', views.editProfile, name="edit_profile"),

    path('profile/', views.viewProfile, name="profile"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('create_bill/', views.createBill, name="create_bill"),
    path('update_bill/<str:pk>/', views.updateBill, name="update_bill"),
    path('delete_bill/<str:pk>/', views.deleteBill, name="delete_bill"),


    path('reset_password', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),

  
]

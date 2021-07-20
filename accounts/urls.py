from accounts.views import lecturer_signup, sign_in
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = "accounts"

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-in/', sign_in, name='sign_in'),
    path('lect-sign-up/', lecturer_signup, name='lecturer_signup'),
     path('stud-sign-up/', auth_views.LogoutView.as_view(), name='student_signup'),
    path('complete-profile/', complete_profile, name='complete_profile'),
]
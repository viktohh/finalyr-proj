from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.sign_in, name="sign_in"),
    path("lecturer-sign-up/", views.lecturer_signup, name="lecturer_signup"),
    path("student-sign-up/", views.student_signup, name="student_signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("validate-username/", views.validate_username, name="validate_username"),
    path("validate-email/", views.validate_email, name="validate_email"),
    path("sent/", views.activation_sent_view, name="activation_sent"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    # path('complete-profile/', complete_profile, name='complete_profile'),
]

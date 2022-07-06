from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import LogoutAPIView, LoginAPIView, user_detail, RegisterView, UpdateProfileView, user_list, UserChangePasswordView, SendPasswordResetEmailView,\
    UserPasswordResetView

urlpatterns = [
    path('users/', user_list),
    path('user-detail/', user_detail),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('change-user/<int:pk>/', UpdateProfileView.as_view(), name='change-password'),
]

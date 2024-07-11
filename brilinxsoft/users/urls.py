from django.urls import path, include
from .views import get_request_user, get_user_by_id, delete_admin_user, send_invite_to_be_admin, ChangePasswordView, LoginView

urlpatterns = [
    path('auth-api/', include('rest_framework.urls')),
    path('get-request-user/', get_request_user, name='get-request-user'),
    path('get-user/<int:user_id>/', get_user_by_id, name='get-user-by-id'),
    path('delete-admin-user/<int:admin_id>/', delete_admin_user, name='delete-admin-by-id'),
    path('set-password/<int:user_id>/', ChangePasswordView.as_view(), name='set-password'),
    path('send-invite-mail/', send_invite_to_be_admin, name='send-invitation-mail'),
    path('login-api/', LoginView.as_view(), name='login-api')
]
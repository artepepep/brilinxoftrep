from django.urls import path, include
from .views import get_request_user, get_user_by_id

urlpatterns = [
    path('auth-api/', include('rest_framework.urls')),
    path('get-request-user/', get_request_user, name='get-request-user'),
    path('get-user/<int:user_id>/', get_user_by_id, name='get-user-by-id')
]
from django.urls import path
from .views import send_email, send_email_pp

urlpatterns = [
    path('send-email/', send_email, name='send-mail'),
    path('send-email-pp/', send_email_pp, name='send-mail-pp'),
]
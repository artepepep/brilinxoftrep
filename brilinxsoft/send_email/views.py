from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmailSerializer
from brilinxsoft.settings import EMAIL_HOST_USER

@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        company_name = request.data.get('company_name')
        interested_service = request.data.get('interested_service')
        details = request.data.get('details')

        message = f"Name: {name}\nEmail: {email}\nClient company: {company_name}\nService: {interested_service}\nProject Details: \n{details}"
    
        send_mail(
            'BRILINXOFT New Client !!!',
            message,
            EMAIL_HOST_USER,
            [EMAIL_HOST_USER],
            fail_silently=False,
        )

        return Response({'message': 'Email sent successfully.'})
    else:
        
        return Response({'message': 'Method not allowed.'}, status=405)
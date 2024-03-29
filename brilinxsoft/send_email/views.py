from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
            'brilinxoft@gmail.com',
            ['brilinxoft@gmail.com'],
            fail_silently=False,
        )

        return Response({'message': 'Email sent successfully.'})
    else:
        return Response({'message': 'Method not allowed.'}, status=405)

@api_view(['POST'])
def send_email_pp(request):
    if request.method == 'POST':
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        email_message = f"Name: {name}\nEmail: {email}\nClient message:\n{message}"

        send_mail(
            'BRILINXOFT New Client(privacy policy)',
            email_message,
            'brilinxoft@gmail.com',
            ['brilinxoft@gmail.com'],
            fail_silently=False,
        )
        
        return Response({'message': 'Email sent successfully.'})
    else:
        return Response({'message': 'Method not allowed.'}, status=405)
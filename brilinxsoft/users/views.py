from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

from .permissions import IsSuperAdmin
from .models import Users
from .service import generate_password, get_username_from_email

@api_view(['GET'])
def get_request_user(request):
    current_user = request.user

    if request.method == 'GET':
        if not current_user.is_anonymous:
            return Response({'request_user': 'is_authenticated', 'user_id': current_user.id}, status=200)
        else:
            return Response({'request_user': 'is_unknown'}, status=200)
    else:
        return Response({'error_message': 'allowed only GET method'}, status=405)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_user_by_id(request, *args, **kwargs):
    user_id = kwargs.get('user_id', None)
    target_user = Users.objects.get(id=user_id)
    if user_id is not None:
        return Response({'user_id': target_user.id, 'username': target_user.username})
    return Response(Users.objects.none())


@api_view(['DELETE'])
@permission_classes((IsSuperAdmin, ))
def delete_admin_user(request, *args, **kwargs):

    if request.method == 'DELETE':
        admin_id = kwargs.get('admin_id', None)
        target_admin = Users.objects.get(id=admin_id)

        if target_admin is not None:
            target_admin.delete()
            return Response({'message': 'user have been deleted'}, status=200)
        
        return Response({'message': f'there is not user with id {admin_id}'})
    else:
        return Response({'message': f'{request.method} not allowed'}, status=405)


@api_view(['POST'])
# @permission_classes((IsSuperAdmin, ))
def send_invite_to_be_admin(request):
    if request.method == 'POST':

        email = request.data.get('email')
        dev_role = request.data.get('developer_role')
        username = get_username_from_email(email)
        password = generate_password(12)
        hashed_password = make_password(password)
        Users.objects.create(username=username, email=email, password=hashed_password, admin_role='Admin', dev_role=dev_role, is_staff=True)

        email_message = f"Congratulations!\nYou have been invited to brilinxoft company, on role of {dev_role}\nNow you are a part of our team, so you can go by the following link to your admin panel\nYour Username: {username}\nYour Email: {email}\nYour password: {password}"
        send_mail(
            "Congratulations! Brilinxoft company",
            email_message,
            'brilinxoft@gmail.com',
            [email],
            fail_silently=False,
        )
        
        return Response({'message': 'email have been sent successfully'}, status=200)
    else:
        return Response({'message': 'Method not allowed.'}, status=405)
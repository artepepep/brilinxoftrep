from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users


@api_view(['GET'])
def get_request_user(request):
    current_user = request.user
    print(current_user)

    if request.method == 'GET':
        if not current_user.is_anonymous:
            return Response({'request_user': 'is_authenticated', 'user_id': current_user.id})
        else:
            return Response({'request_user': 'is_unknown'})
    else:
        return Response({'error_message': 'allowed only GET method'})


@api_view(['GET'])
def get_user_by_id(request, *args, **kwargs):
    user_id = kwargs.get('user_id', None)
    target_user = Users.objects.get(id=user_id)
    if user_id is not None:
        return Response({'username': target_user.username})
    return Response(Users.objects.none())
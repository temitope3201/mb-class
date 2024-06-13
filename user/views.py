from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from drf_yasg.utils import swagger_auto_schema


from rest_framework.permissions import AllowAny
  
from main.models import Recipe
from user.serializers import *
from user.models import CustomUser


@swagger_auto_schema(method='post', request_body=SignUpSerializer)
@api_view(['POST'])
def sign_up(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        email = serializer.validated_data["email"]
        phone_number = serializer.validated_data["phone_number"]
        address = serializer.validated_data["address"]
        account_type = serializer.validated_data["account_type"]

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username,
         email=email, phone_number=phone_number, address=address, account_type=account_type)
        #user.save()

        user.set_password(password)
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        #remember to fix this section
        #token = "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
        ###################

        return Response({"status": True, "token": token.key}, status=status.HTTP_201_CREATED)


    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=SignInSerializer)
@api_view(['POST'])
#@permission_classes([AllowAny])
def sign_in(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    print(user)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"msg": "Sign in successful", "token": token.key}, status=status.HTTP_201_CREATED)

    else:
        return Response({"error": "Invalid logins"}, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)})
@api_view(['GET'])
def all(request):
    pass


@swagger_auto_schema(method='put', request_body=UserSerializer, responses={200: UserSerializer()})
@api_view(['PUT'])
def update_user(request, user_id):
    pass


@swagger_auto_schema(method='delete', responses={204: 'No content'})
@api_view(['DELETE'])
def delete_user(request, user_id):
    pass


@swagger_auto_schema(method='get', responses={200: UserSerializer()})
@api_view(['GET'])
def get_user_detail(request, user_id):
    pass

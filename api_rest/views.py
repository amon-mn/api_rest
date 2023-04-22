from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UserSerializer

import json


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = Usuario.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = UserSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def get_by_login(request, login):

    try:
        user = Usuario.objects.get(pk=login)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)




# CRUDZAO DA MASSA
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['user']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                login = request.GET['user']         # Find get parameter

                try:
                    user = Usuario.objects.get(pk=login)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_user = request.data
        
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        login = request.data['user']

        try:
            updated_user = Usuario.objects.get(pk=login)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            user_to_delete = Usuario.objects.get(pk=request.data['login'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

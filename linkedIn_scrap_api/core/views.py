from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer

# Create your views here.
from internal_code.scrap_voyager import scrap_connections


class PostView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer_data = serializer.data
            user_id_string = serializer_data['linkedIn_email']
            password_string = serializer_data['linkedIn_password']
            # print(user_id_string, password_string)
            all_connection_details = scrap_connections(user_id_string, password_string)
            # print(all_connection_details)
            return Response(all_connection_details)
        else:
            return Response(serializer.errors)

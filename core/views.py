from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserDetail
from .serializers import UserDetailsSerializer
from rest_framework import status as st
# Create your views here.

class UserDetailsView(APIView):
    def post(self, request):
        try:
            request_data = request.data
            if request_data.get("username"):
                user = UserDetail.objects.create(username=request_data.get("username"))
                serializer = UserDetailsSerializer(data = user)

                if serializer.is_valid():
                    data = serializer.data
                    status = True
                    status_code = st.HTTP_200_OK
                    message = f"User Registered Successfully"
                    errors = {}
                else:
                    data = {}
                    status = False
                    status_code = st.HTTP_400_BAD_REQUEST
                    message = f"User Not Registered"
                    errors = serializer.errors
            else:
                data = {}
                status = False
                status_code = st.HTTP_400_BAD_REQUEST
                message = f"User Not Registered"
                errors = "Add User Details"
        except Exception as e:
            data = {}
            status = False
            status_code = st.HTTP_500_INTERNAL_SERVER_ERROR
            message = f"User Not Registered"
            errors = e
        return JsonResponse({'status':status, "message":message, 'data':data, 'status_code': status_code, 'errors':errors})
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from rest_framework.views import APIView
from .models import * 
from .serializers import * 
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['GET'])

def home(request):
    student_obj = student.objects.all()
    serializer = studentSerializer(student_obj,many=True)
    return Response({'status':200,'payload':serializer.data})

class registerUser(APIView):
    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializer.data,'token': str(token_obj),'message':'data received'})
        

class studentAPI(APIView):

    def get(self,request):
        student_obj = student.objects.all()
        serializer = studentSerializer(student_obj,many=True)
        return Response({'status':200,'payload':serializer.data})

    def post(self,request):
        data=request.data
        serializer = studentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()

        return Response({'status':200,'payload':data,'message':'data received'})

    def put(self,request):
        try:
            student_obj = student.objects.get(id=request.data['id'])
            data=request.data
            serializer = studentSerializer(student_obj, data=request.data)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
            serializer.save()

            return Response({'status':200,'payload':data,'message':'data received'})

        except Exception as e:
             print(e)
             return Response({'status':403,'message':'invalid id'})

    def patch(self,request):
        try:
            student_obj = student.objects.get(id=request.data['id'])
            data=request.data
            serializer = studentSerializer(student_obj, data=request.data , partial=True)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
            serializer.save()

            return Response({'status':200,'payload':data,'message':'data received'})

        except Exception as e:
             print(e)
             return Response({'status':403,'message':'invalid id'})

    
    def delete(self,request):
        try:
            student_obj = student.objects.get(id=id)
            student_obj.delete()
            return Response({'status':200,'message':'Deleted data successfully '})
    
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})















"""
@api_view(['POST'])

def post_data(request):
    

@api_view(['PUT'])

def update_data(request,id):
    
@api_view(['DELETE'])

def delete_data(request,id):
    try:
        student_obj = student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200,'message':'Deleted data successfully '})
 
    except Exception as e:
        print(e)
        return Response({'status':403,'message':'invalid id'})

"""
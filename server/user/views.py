from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views,status
from .serializers import userSerializer
import bcrypt,jwt,datetime
from .models import User


#Create your views here.

class signUP(views.APIView):
    def post(self,request):
        body = userSerializer(data=request.data)
        
        body.is_valid(raise_exception=True)
        
        # encrypt user password
        password = request.data['password']
        hashPassword = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt());
        
        
        
        body.validated_data['password']=hashPassword.decode('utf-8')
        body.save()
        
        
        return Response(body.data)
class signIn(views.APIView):
    def post(self,request):
        email = request.data['email']
        password=request.data['password']
        findUser = User.objects.filter(email=email).first()
        if findUser is None:
           return Response({"message":"User is not found","status":status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        
        #Compare the provided password with the hashed password
        
        checkPassword = bcrypt.checkpw(password.encode('utf-8'), findUser.password.encode('utf-8'))
        
        if not checkPassword:
            return Response(
                {"message": "Password is incorrect", "status": "409", "error": "True"},
                status=status.HTTP_409_CONFLICT,
            )
            
        #create token
        
        payload = {
            'id': str(findUser.id),  # Convert UUID to string
            'isAdmin':bool(findUser.is_superuser),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.set_cookie(key='ene', value=token, httponly=True,samesite=None,secure=True)
        serializer=userSerializer(findUser)
        response.data=serializer.data
        return response


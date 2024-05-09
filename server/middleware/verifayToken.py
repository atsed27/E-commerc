from django.http import HttpResponseForbidden,HttpResponseNotFound
import jwt
from user.models import User


class VerifyToken:
     def __init__(self, get_response):
        self.get_response = get_response
    
     def __call__(self, request,*args,**kwargs):
        # Get the token from the request
        token = request.COOKIES.get('ene')
       
         # Validate the token
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
          
            #check user in Database
            findUser = User.objects.filter(id=payload['id']).first()
            print(findUser)
            if findUser is None:
                return HttpResponseNotFound('user is not found')
            # Add the user ID to the request for further processing
            request.userId = payload['id']
            request.isAdmin=payload['isAdmin']
            print(request.userId,request.isAdmin)
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid token')

        return self.get_response(request,*args, **kwargs)
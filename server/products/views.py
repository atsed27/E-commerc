from django.shortcuts import render
from rest_framework import views,status
from .serializers import ProductSerializer
from rest_framework.response import  Response
from user.models import User
from .models import Product
import os
from dotenv import load_dotenv

# Create your views here.


load_dotenv()


class Products(views.APIView):
    #Get all Product
    def get(self,request):
        #find all product
        man=request.GET.get('man')
        woman=request.GET.get('woman')
        electron=request.GET.get('electron')
        child=request.GET.get('child')
        #find man product
        if man:
            findProduct = Product.objects.filter(category=man)
            serializer=ProductSerializer(findProduct,many=True)
            return Response(serializer.data)
        if woman:
            findProduct = Product.objects.filter(category=woman)
            serializer=ProductSerializer(findProduct,many=True)
            return Response(serializer.data)
        if child:
            findProduct = Product.objects.filter(category=child)
            serializer=ProductSerializer(findProduct,many=True)
            return Response(serializer.data)
         
        if electron:
            findProduct = Product.objects.filter(category=electron)
            serializer=ProductSerializer(findProduct,many=True)
            return Response(serializer.data)
        
        findProduct=Product.objects.all()
        serializer=ProductSerializer(findProduct,many=True)
        return Response(serializer.data)
    
    
    #create product
    def post(self,request):
       try:
            #check serializers
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
       
            #find User
            findUser=User.objects.filter(id=request.userId).first()
        
           #If user is Admin
            print(request.isAdmin)
            if request.isAdmin:
               serializer.save(user=findUser)
               return Response(serializer.data)
            else: 
                return Response({"message":"Add Product only Admin","error":"True","status":"403"},status=status.HTTP_403_FORBIDDEN)
       except Exception as e:
           # Create an error dictionary with relevant information
        error_dict = {
            'error_type': type(e).__name__,
            'error_message': str(e),
            'exception_location': str(e.__traceback__.tb_frame.f_code),
          
        }

        # Return the error response as JSON
        return Response(error_dict, status=500)
        
    #Update product
    def put(self,request,pk):
         #find product 
        findProduct = Product.objects.filter(id=pk).first()
        
        if findProduct is None:
             return Response({"message":"Product is not Found","error":"True","status":"404"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=ProductSerializer(findProduct,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
     
       
        if((request.userId)==str(findProduct.user.id)):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
          return Response({"message":"Product cant only update admin","error":"True","status":"403"},status=status.
                          HTTP_403_FORBIDDEN)
    
    #Delete product 
    def delete(self,request,pk):
         #find product 
        findProduct = Product.objects.filter(id=pk).first()
        
        if findProduct is None:
             return Response({"message":"Product is not Found","error":"True","status":"404"},status=status.HTTP_404_NOT_FOUND)
        
        if((request.userId)==str(findProduct.user.id)):
            Product.objects.filter(id=pk).delete()
            return Response({"message":" delete is sucssfully","error":"True","status":"403"},status=status.HTTP_200_OK)
        else:
          return Response({"message":"you can't delete this product","error":"True","status":"403"},status=status.
                          HTTP_403_FORBIDDEN)
        
class ProductPart(views.APIView):
    #Get one Product
    def get(self,request,pk):
        
        findProduct=Product.objects.filter(id=pk).first()
        if  not findProduct:
            return Response({"message":"Product is not found","status":status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(findProduct)
        return Response(serializer.data)
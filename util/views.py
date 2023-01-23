from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Province
from .serializers import Province_Serializer
# Create your views here.

class Province_View(APIView):
    
    def post(self, request,  *args, **kwargs):
        
        serializer = Province_Serializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'success': True,
                'status_code': 201,
                'message': 'Provincia criada com sucesso.',
                'data': serializer.data
            }
            return Response(response, status=201)
    
    def get(self, request,  *args, **kwargs):
        queryset = Province.objects.all()
        data = Province_Serializer(queryset, many=True).data
        response = {
                'success': True,
                'status_code': 200,
                'message': 'Provincias.',
                'data': data,
            }
        return Response(response, status=200);
    
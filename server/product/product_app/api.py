from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Product
from account.authenticate import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"created Objects successfully{serializer.data}")
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def show_product(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset,many=True)
    logger.info(f"Objects show successfully")
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def retrieve_product(request,pk):
    obj = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(obj)
    logger.info(f"Objects get succefully {obj}")
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def update_product(request,pk):
    obj = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(obj,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Update Objects successfully:{serializer.data}")
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def delete_product(request,pk):
    obj = get_object_or_404(Product,id=pk)
    logger.info(f"Delete Objects successfully:{obj}")
    obj.delete()
    return Response(data=None,status=status.HTTP_200_OK)
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Category, Cast, Series
from .serializers import MovieSerializer, CategorySerializer, CastSerializer, SeriesSerializer

@api_view(['GET','POST'])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def movie_detail_update_delete (request,pk):
    try:
        movie=Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer=MovieSerializer(movie,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def series_list_create(request):
    if request.method == 'GET':
        seriess = Series.objects.all()
        serializer = SeriesSerializer(seriess, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=SeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def series_detail_update_delete (request,pk):
    try:
        series=Series.objects.get(pk=pk)
    except Series.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=SeriesSerializer(series)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=SeriesSerializer(series, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer=SeriesSerializer(series,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer, ArtistUpdateSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        artist.delete()
        data = {
            'delete': f'등록 번호 {artist_pk} 번의 {artist.name}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search(request):
    is_group_param = request.query_params.get('is_group')
    artists = Artist.objects.all() # 모든 아티스트를 가지고 온 다음


    # None 인경우 가정해서 체크도 해줘보기!
    invalid_artists = artists.filter(is_group__isnull=True)
    if invalid_artists.exists():
        return Response({'error': '데이터가 잘못되었습니다.'}, status=400)

    if is_group_param is not None:
        if is_group_param.lower() == 'true':
            artists = artists.filter(is_group=True)
        elif is_group_param.lower() == 'false':
            artists = artists.filter(is_group=False)
        else:
             return Response({'error': '잘못된 쿼리 파라미터입니다.'}, status=400)

    
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
    

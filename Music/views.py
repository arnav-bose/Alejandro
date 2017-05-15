from django.shortcuts import render, get_object_or_404
from.models import Album

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Song
from .serializers import SongSerializer


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'Music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'Music/details.html', {'album': album})

class SongList(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self):
        pass

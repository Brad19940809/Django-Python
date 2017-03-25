from django.shortcuts import render
from django.http import HttpResponse
from music.models import Album
from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id):
    return HttpResponse('<h2>Details for Album id:' + album_id+'</h2>')

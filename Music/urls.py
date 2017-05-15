from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'music'

urlpatterns = [
    # Home Page for Music
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/71/
    url(r'^(\d+)/$', views.detail, name='detail'),

    # /music/71/favorite/
    #url(r'^(\d+)/favorite/$', views.favorite, name='favorite'),

    url(r'^songs/', views.SongList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
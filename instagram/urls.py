from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

 url(r'^$', views.newsfeed, name='allslygram'),
 url(r'^accounts/profile/', views.profile, name ='myProfile'),
 url(r'^new/story/(?P<username>[-_\w.]+)$', views.new_story, name='newStory'),
 url(r'^user/(\d+)', views.profile, name='Profiles'),
 url(r'^image/(\d+)', views.single_pic, name='singlePic'),
 url(r'^profile/', views.profile, name='Profile'),
 url(r'^single_image/likes/(\d+)', views.single_image_like, name='singlePicLike'),
 url(r'^new/comment/(?P<username>[-_\w.]+)$', views.new_comment, name='new_Comment'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

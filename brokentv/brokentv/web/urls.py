from django.urls import path

from brokentv.web.views import ShowIndex, ShowNewIndex, ShowPost

urlpatterns = (
    path('', ShowIndex.as_view(), name='show index'),
    path('new/', ShowNewIndex.as_view(), name='show new index'),
    path('post/', ShowPost.as_view(), name='show post'),
)


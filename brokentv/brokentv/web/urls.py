from django.urls import path

from brokentv.web.views import ShowIndex, ShowNewIndex

urlpatterns = (
    path('', ShowIndex.as_view(), name='show index'),
    path('new/', ShowNewIndex.as_view(), name='show new index'),
)


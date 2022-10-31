from django.urls import path

from brokentv.web.views import ShowIndex

urlpatterns = (
    path('', ShowIndex.as_view(), name='show index'),
)


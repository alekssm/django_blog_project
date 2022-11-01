from django.urls import path

from brokentv.web.views import ShowIndex, ProfileDetailsView

urlpatterns = (
    path('', ShowIndex.as_view(), name='show index'),
    path('profile/int:<pk>/', ProfileDetailsView.as_view(), name='profile details'),
)


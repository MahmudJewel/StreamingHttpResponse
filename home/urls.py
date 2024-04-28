from django.urls import path

from .views import home, stream_data

urlpatterns = [
    path('', home, name='home'),
    path('stream-data/', stream_data, name='stream_data'),
]
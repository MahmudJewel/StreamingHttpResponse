from django.urls import path

from .views import home, stream_data, my_view, astreaming

urlpatterns = [
    path('', home, name='home'),
    path('stream-data/', stream_data, name='stream_data'),
    path('my_view/', my_view, name='my_view'),
    path('astreaming/', astreaming, name='astreaming'),
]
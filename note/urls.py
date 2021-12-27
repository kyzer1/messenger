from django.urls import path
from note.views import my_note, recived, send, delete


app_name = 'note'

urlpatterns = [
    path('mynotes', my_note),
    path('recive', recived),
    path('send/<int:id>/<str:name>', send),
    path('delete/<int:id>', delete)

]

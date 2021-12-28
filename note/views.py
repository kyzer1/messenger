from django.core.checks import messages
from django.shortcuts import render

from note.models import Text
from django.http import JsonResponse
from django.contrib.auth.models import User


def my_note(request):
    print(request.user.id)

    notes = {}
    messages = Text.objects.filter(owner_id=request.user.id)

    for text in messages:
        notes[text.id] = text.text

    return JsonResponse(notes)


def recived(request):
    recived = Text.objects.filter(send_to=request.user.id)
    notes = {}

    for text in recived:
        notes[text.id] = text.text

    return JsonResponse(notes)


def send(request, id, name):
    user = User.objects.get(username=name)
    text = Text.objects.get(id=id)

    if text.owner_id == request.user.id:
        if request.user != user:
            text.send_to.add(user)
            return JsonResponse({'done':{}})
        else:
            return JsonResponse({'ERROR': 'be khodet nemitoni befresti'})

    else:
        return JsonResponse({'ERROR': 'bayad male khodet bashe'})
    

def delete(request, id):
    text = Text.objects.get(id=id)
    if text.owner_id == request.user.id:
        text.delete()

    return JsonResponse({'message': 'done'})

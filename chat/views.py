from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from company.models import *
from uuid import uuid4
from chat.models import *


def index(request):
    return render(request, 'chat/index.html', {})


def hitter(request, c_name):
    print(c_name)

    x = Support.objects.filter(company__name__iexact=c_name)
    if x.exists():
        print("yes i have it")
        if request.session.get('room') is None:
            n = str(uuid4())
            n = n.replace('-', "")
            Room.objects.get_or_create(rid=n, created_by=request.user)
            request.session['room'] = n

        else:
            n = request.session.get('room')

    # n = str(uuid4())
    if n is None:
        print("unknown error ocuured")
        return HttpResponse("unknown errror  ocuured")
    else:
        return redirect(reverse('room', kwargs={'c_name': c_name, 'room_name': n}))

    # return redirect(reverse())


def close_chat(request, c_name):
    try:
        del request.session['room']
    except:
        pass
    return HttpResponse(True)


def room(request, c_name, room_name):
    _x = request.session.get('room')
    if _x is None:
        try:
            _y = Room.objects.get(rid=room_name, created_by=request.user)
        except Exception as e:
            print(e)
            _y = None
        if _y is not None:
            request.session['room'] = room_name
            return redirect(reverse('room', kwargs={'c_name': c_name, 'room_name': room_name}))
        else:
            return redirect(reverse('hit', kwargs={'c_name': c_name}))
    # else:

    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })


def room2(request, c_name, room_name):
    # request.session['room']

    return render(request, 'chat/room2.html', {
        'room_name': room_name,
    })

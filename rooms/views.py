from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(req):
    page = req.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(
        req,
        "rooms/home.html",
        context={"rooms": rooms},
    )

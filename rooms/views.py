from django.shortcuts import render
from . import models


def all_rooms(req):
    page = int(req.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(req, "rooms/home.html", context={"rooms": all_rooms})

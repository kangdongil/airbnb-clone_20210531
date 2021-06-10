from datetime import datetime
from django.shortcuts import render


def all_rooms(req):
    now = datetime.now()
    hungry = True
    return render(
        req,
        "all_rooms.html",
        context={
            "now": now,
            "hungry": hungry,
        },
    )

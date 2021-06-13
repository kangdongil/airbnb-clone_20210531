from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


def search(request):

    country = request.GET.get("country")

    if country:

        form = forms.SearchForm(request.GET)

        if form.is_valid():
            print(forms.cleaned_data)
    else:

        form = forms.SearchForm()

    form = forms.SearchForm(request.GET)

    return render(request, "rooms/search.html", {"form": form})

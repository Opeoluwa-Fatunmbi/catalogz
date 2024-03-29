from django.shortcuts import render
from apps.gallery.models import Media
from django.views import View
from django.views.generic import ListView
from django.db.models import QuerySet

# from apps.gallery.models import Product
# from apps.gallery.utils import sort_products, sort_filter_value
from django.http import Http404


# Create your views here.


class HomeView(View):
    def get(self, request):
        media = Media.objects.all()[:6]
        context = {
            "media": media,
        }
        return render(request, "gallery/home.html", context)


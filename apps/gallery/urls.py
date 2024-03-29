from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
#    path("media/", views.HomeView.as_view(), name="products"),
#    path("media/<slug:slug>/", views.ProductView.as_view(), name="product-detail"),
]

from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Track"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Product View"),
    path("checkout/", views.checkout, name="CheckOut"),
]
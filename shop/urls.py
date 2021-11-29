from .import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About US"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="tracking status"),
    path("search/", views.search, name="searching"),
    path("productview/", views.productview, name="productview"),
    path("checkout/", views.checkout, name="checkout")
]
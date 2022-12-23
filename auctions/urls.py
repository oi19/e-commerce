from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # API Rout
    path("listing/<int:lis_id>", views.listing, name="listing"),
    path("watchlist/<int:lis_id>", views.watchlist, name="watchlist"),
    path("create", views.create, name="create"),
    path("remove/<int:lis_id>", views.remove, name="remove"),
    path("comments/<int:lis_id>", views.comments, name="comments"),
    # API Rout
    path("close/<int:lis_id>", views.close, name="close"),
    path("cat", views.cat, name="cat"),
    path("cat/<str:category>", views.cat_product, name="cat_product"),

]

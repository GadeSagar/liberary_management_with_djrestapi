from django.urls import path
from.import views


urlpatterns = [
    path("",views.login,name="login"),
    path("register",views.register , name="register"),
    path("logout", views.logout,name="logout"),
    path("home",views.home , name  ="home"),
    path("update/<int:id>",views.update , name = "update"),
    path("delete_book/<int:id>",views.delete_book , name = "delete_book"),
    path("add",views.add , name = "add")
]
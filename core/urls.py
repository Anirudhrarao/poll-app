from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home-page"),
    path('regsiter/',views.signup,name="register-page"),
    path('login/',views.signin,name="login-page"),
    path('logout/',views.logout_view,name="logout-page"),
    path('profile/',views.profile,name="profile-page"),
    path('poll/',views.poll_view,name="poll-page"),
    path('create/',views.create_poll,name="create-page"),
    path('vote/<question_id>/',views.vote,name="vote-page"),
    path('result/<question_id>/',views.result,name="result-page"),
]

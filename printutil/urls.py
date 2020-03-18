from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as authviews

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('files/source/<username>/<filename>', views.source_view, name='files'),
    path('print/<username>/<filename>', views.print_view, name='print'),
    path('login/', authviews.LoginView.as_view(template_name="login.html", authentication_form=LoginForm, redirect_authenticated_user=True), name='login'),
    path('logout/', authviews.LogoutView.as_view(), name='logout'),
]

handler404 = views.handler404
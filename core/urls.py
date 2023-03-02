from django.urls import path
from .views import UserDetailsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('user/', csrf_exempt(UserDetailsView.as_view())),
]
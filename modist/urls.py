from django.urls import path
from modist.views import MainView

urlpatterns = [
    path('', MainView.as_view())
]
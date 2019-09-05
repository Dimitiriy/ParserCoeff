from django.urls import path
from .views import index, update
from .views import MatchesListView

urlpatterns = [
    path('', MatchesListView.as_view(), name='index'),
    path('update/', update, name='update'),
]

from django.urls import path
from .views import LendingListView

urlpatterns = [
    path('', LendingListView.as_view(), name="lending_template"),
] 
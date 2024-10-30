from django.urls import path
from . import views


urlpatterns = [
    path(
        "accounts/",
        views.AccountListCreateAPIView.as_view(),
        name="account_create_list",
    ),
    path(
        "account/<str:pk>/",
        views.AccountRetrieveUpdateDestroyAPIView.as_view(),
        name="account_detail",
    ),
]

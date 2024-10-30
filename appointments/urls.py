from django.urls import path
from . import views


urlpatterns = [
    path(
        "appointments/",
        views.AppointmentListCreateAPIView.as_view(),
        name="appoitment_create_list",
    ),
    path(
        "appoitment/<str:pk>/",
        views.AppointmentRetrieveUpdateDestroyAPIView.as_view(),
        name="appoitment_detail",
    ),
]

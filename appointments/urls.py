from django.urls import path
from . import views


urlpatterns = [
    path(
        "appointments/",
        views.AppointmentListCreateAPIView.as_view(),
        name="appoitment_create_list",
    ),
    path(
        "user-appointments/",
        views.UserAppointmentListAPIView.as_view(),
        name="user_appoitment_create_list",
    ),
    path(
        "professional-appointments/<uuid:pk>/",
        views.ProfessionalAppointmentListAPIView.as_view(),
        name="professional_appoitment_create_list",
    ),
    path(
        "appoitment/<uuid:pk>/",
        views.AppointmentRetrieveUpdateDestroyAPIView.as_view(),
        name="appoitment_detail",
    ),
]

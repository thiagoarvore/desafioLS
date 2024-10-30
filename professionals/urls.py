from django.urls import path
from . import views


urlpatterns = [
    path(
        "professionals/",
        views.ProfessionalListCreateAPIView.as_view(),
        name="professional_create_list",
    ),
    path(
        "professional/<str:pk>/",
        views.ProfessionalRetrieveUpdateDestroyAPIView.as_view(),
        name="professional_detail",
    ),
]

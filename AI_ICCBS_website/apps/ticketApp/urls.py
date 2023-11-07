from django.urls import path
from . import views

app_name = "ticketApp"
urlpatterns = [
    path('', views.ICCBSITticketstatus, name='ICCBSITticketstatus'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
]







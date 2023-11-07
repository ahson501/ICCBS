from django.shortcuts import render
from .models import Ticket
from django.http import HttpResponse

def ICCBSITticketstatus(request:HttpResponse):
 tickets = Ticket.objects.order_by('-created_at')[:25]
 return render(request,'ICCBSITticketstatus.html', {'tickets': tickets})

def ticket_by_id(request:HttpResponse, ticket_id):
 ticket = Ticket.objects.get(pk=ticket_id)
 return render(request, 'ticket_by_id.html', {'ticket':ticket})

 
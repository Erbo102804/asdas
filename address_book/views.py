from django.shortcuts import render, get_object_or_404
from .models import Contact

def contact_list(request):


    contacts = Contact.objects.all()
    return render(request, 'address_book/contact_list.html', {'contacts': contacts})

def contact_detail(request, contact_id):


    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'address_book/contact_detail.html', {'contact': contact})


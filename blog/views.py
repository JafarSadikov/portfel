from django.shortcuts import redirect, render


from .models import Clients
from .forms import ClientsForm


def register_clients(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = ClientsForm()
    return render(request, 'browny-v1.0/index.html', {'form': form})
    
    
    

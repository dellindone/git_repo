from django.shortcuts import render
from .models import ChaiVerity, Store
from .forms import ChaiVerityForm
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = ChaiVerity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVerity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVerityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_verity']
            stores = Store.objects.filter(chai_verities=chai_variety)
    else:
        form = ChaiVerityForm()
    return render(request, 'chai/chai_stores.html', {'stores':stores, 'form':form})
from django.shortcuts import render, get_object_or_404
from usedcars_app.models import Car
# Create your views here.



def car_list(request):
    cars = Car.objects.all()
    return render(request, 'usedcars_app/carlist.html', {'cars': cars})

def car_detail(request,id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'usedcars_app/cardetail.html', {'car': car})

def car_search(request):
    query = request.GET.get('q')
    results = Car.objects.filter(make__icontains=query) | Car.objects.filter(model__icontains=query) | Car.objects.filter(location__icontains=query)
    return render(request, 'usedcars_app/search.html', {'results': results, 'query': query})

from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render (request, 'home.html')

def recipieView(request):
    recipies = Recipie.objects.all()
    context = {'recipies':recipies}
    return render (request, 'recipie_view.html', context)

def add_recipie(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('recipie_name')
        ingredants = data.get('recipie_ingrediants')
        ingrediants = [i.strip() for i in ingredants.split(',')]
        desc = data.get('recipie_description')
        img = request.FILES.get('recipie_image')

        Recipie.objects.create(recipie_name = name, 
                               recipie_ingrediants = ','.join(ingrediants), 
                               recipie_description = desc, 
                               recipie_image = img)

        return redirect('recipieView')
    return render (request, 'add_recipie.html')


def recipie_description(request, recipie_id):
    recipie = get_object_or_404(Recipie, pk = recipie_id)
    ingrediants = [i.strip() for i in recipie.recipie_ingrediants.split(',')]
    return render (request, 'recipie_description.html', {'recipie': recipie, 'ingrediants': ingrediants})

def update_recipie(request, recipie_id):
    recipie = get_object_or_404(Recipie, id=recipie_id)


    if request.method == 'POST':
        data = request.POST
        name = data.get('recipie_name')
        ingredants = data.get('recipie_ingrediants')
        ingrediants = [i.strip() for i in ingredants.split(',')]
        desc = data.get('recipie_description')
        img = request.FILES.get('recipie_image')

        recipie.recipie_name = name
        recipie.recipie_ingrediants = ingredants
        recipie.recipie_description = desc
        if img:
            recipie.recipie_image = img

        recipie.save()
        return redirect('recipieView')
    
    return render (request, 'update_recipie.html', {'recipie': recipie})    

def delete_recipie(request, recipie_id):
    recipie = get_object_or_404(Recipie, id = recipie_id)
    recipie.delete()
    return redirect(recipieView)

from django.shortcuts import render, redirect
from datetime import datetime
from .models import dish, owner, group
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import dish

def index(request):
    dishs = dish.objects.all()
    owners = owner.objects.all()
    groups = group.objects.all()
    new = dishs.count()+1

    if request.method == "POST":
        dish_id = new
        dish_name = request.POST.get('dish_name')
        dish_size = request.POST.get('dish_size')
        dish_price = request.POST.get('dish_price')
        dish_description = request.POST.get('dish_description')
        # dish_image = request.POST.get('dish_image')
        dish_image = request.FILES.get('dish_image')
        dish_category = request.POST.get('dish_category')
        item = dish(dish_id = dish_id, dish_name = dish_name, dish_size = dish_size, dish_price = dish_price, dish_description = dish_description,dish_category=dish_category, dish_image = dish_image) 
        item.save()
    params = {'dish': dishs, 'owner': owners, 'group': groups}
    return render(request, "card/index.html", params)

def category(request):
    dishs = dish.objects.all()
    owners = owner.objects.all()
    groups = group.objects.all()


    if request.method == "POST":
        dish_get = request.POST.get('dish_category')
        get_category = dish_get.lower()
        dish_category = get_category.replace(" ", "_")
        item = group(dish_category = dish_category) 
        item.save()
    params = {'dish': dishs, 'owner': owners, 'group': groups}
    # return render(request, "card/index.html", params)
    return render(request, "card/check.html", params)


def check(request):

    owners = owner.objects.all()
    groups = group.objects.all()
    dishs = dish.objects.all()
    for o in owners:
        if request.method == "POST":
            name = request.POST.get('name')
            password = request.POST.get('password')
            if o.name == name and o.password == password :
                params = {'dish': dishs, 'owner': owners, 'group':groups}
                return render(request, "card/check.html", params)
            # else : 
            #     params = {'dish': dishs, 'owner': owners, 'group':groups}
            #     return HttpResponseRedirect(reverse('index'))
# def categ(request):
#     categorys = category.objects.all()
#     if request.method == "POST":
#         dish_category = request.POST.get('dish_category')
#         item = category(dish_category=dish_category)
#         item.save()
#         return HttpResponseRedirect(reverse('check'))

    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #     if owners.name == name and owners.password == password :

def delete(request, id):
    dishes = dish.objects.get(id=id)
    dishes.delete()
    return reverse('index')
# def delete(request, id):
#     dishs = dish.objects.get(id=id)
#     dishs.delete()

#     all_dishes = dish.objects.all()
#     for i, dish in enumerate(all_dishes):
#         dish.dish_id = i + 1
#         dish.save()
    
#     return HttpResponseRedirect(reverse('check'))

def update(request, id):
    # dishs = dish.objects.get(id=id)
    # template = loader.get_template('update.html')
    # context = {
    #     'dishs': dishs,
    # }
    # return HttpResponse(template.render(context, request))
    dish_name = request.POST['dish_name']
    dish_category = request.POST['dish_category']
    dish_size = request.POST['dish_size']
    dish_price = request.POST['dish_price']
    dish_description = request.POST['dish_description']
    dish_image = request.FILES['dish_image']
    dishs = dish.objects.get(id=id)
    dishs.dish_name = dish_name
    dishs.dish_category = dish_category
    dishs.dish_size = dish_size
    dishs.dish_description = dish_description
    dishs.dish_price = dish_price
    dishs.dish_image = dish_image
    dishs.save()
    return HttpResponseRedirect(reverse('index'))
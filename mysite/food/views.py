from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# here we are importing generic views ListView --- it is something which is default given by django
from django.views.generic.list import ListView
# here we are importing generic detail view provided by django
from django.views.generic.detail import DetailView

# Create your views here.
# ------------------------------------------------------------
# this follwing is called as function based views 
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html', context)
                  
                    # OR

# this follwing is called as class based views
class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name ='item_list'

# ---------------------------------------------------------------


def item(request):
    return HttpResponse('<h1>this is anothere item<h1>')

def thing(request):
    return HttpResponse('Hey hi i am Krunal Kolhe, i am welcoming you to my django website')

# -------------------------------------------------------------
# this is the function based detail view
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item': item,
    }
    return render(request, 'food/detail.html', context)
                
                #  OR

# this following is the class based detail view

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

# ----------------------------------------------------------------
# we can also create class based views for the following 


def create_item(request):
    # here we are creating object out of that class in forms.py
    form = ItemForm(request.POST or None)


    if form.is_valid():
        form.save()
        return redirect('food:index')


    return render(request, 'food/item-form.html',{'form':form})


def update_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form, 'item':item})



def delete_item(request,id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})
    
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Category, Photo


# Create your views here.

def gallary(request):
    category = request.GET.get('category')
    if category == None:
       photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(Category__name=category)  
   

    categories = Category.objects.all()
    
    # photos = Photo.objects.all()
    
    context = {'cata': categories, 'poths':photos}

    return render(request, 'gallary/gallary.html', context)

def photov(request, pk):
    photo = Photo.objects.get(id=pk)
    
   
    context = {'photos':photo}
    print(context)
    return render(request, 'gallary/photoview.html', context)

def deletev(request, pk):
    delete = Photo.objects.get(id=pk)
    delete.delete()
   
    
    return HttpResponseRedirect('/')

def addphotos(request):

    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['Category_new']   != '':
            category , create = Category.objects.get_or_create(name=data['Category_new'])
        else:
         category = None
       
        photo = Photo.objects.create(
            Category = category,
            description = data['description'],
            image = image,
        )
        return redirect('gallary')

    context = {'cata': categories}

    return render(request, 'gallary/addphotos.html',context)

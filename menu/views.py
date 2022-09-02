from django.shortcuts import render , redirect
from .models import Dish , Drink , Pasta , Risotto
# Create your views here.


def index(request):
    return render(request, 'acc/index.html')


def dish(request):
    menu=Dish.objects.all()
    context={
        'menuset':menu
    }
    return render(request, 'menu/dish.html',context)

def pasta(request):
    menu=Pasta.objects.all()
    context={
        'menuset':menu
    }
    return render(request, 'menu/pasta.html',context)

def risotto(request):
    menu=Risotto.objects.all()
    context={
        'menuset':menu
    }
    return render(request, 'menu/risotto.html',context)

def drink(request):
    menu=Drink.objects.all()
    context={
        'menuset':menu
    }
    return render(request, 'menu/drink.html',context)

def dish(request):
    menu=Dish.objects.all()
    context={
        'menuset':menu
    }
    return render(request, 'menu/dish.html',context)

def detail(request,mpk):
    context={
    }
    try: 
        Dish.objects.get(name=mpk)
        odi=Dish.objects.get(name=mpk)
        context.update({
            'o':odi
        })
    except:
        pass
    try :
        Pasta.objects.get(name=mpk)
        opa=Pasta.objects.get(name=mpk)
        context.update({
            'o':opa
        })
    except:
        pass
    try :
        Risotto.objects.get(name=mpk)
        ori=Risotto.objects.get(name=mpk)
        context.update({
            'o':ori
        })
    except:
        pass
    try :
        Drink.objects.get(name=mpk)
        odr=Drink.objects.get(name=mpk)
        context.update({
            'o':odr
        })
    except:
        pass
    return render(request,'menu/detail.html',context)

def create(request):
    mt=request.POST.get('mtype')
    mn=request.POST.get('mname')
    mp=request.POST.get('mpri')
    mpic=request.FILES.get('mpic')
    mc=request.POST.get('mcon')
    type=['pasta','risotto','dish','non_alcohol','alcohol']
    context={
        'list':type
    }
    if request.method=='POST':
        if mt=='dish':
            Dish(name=mn,price=mp,pic=mpic,con=mc).save()
            return redirect('menu:dish')
        elif mt=='pasta':
            Pasta(name=mn,price=mp,pic=mpic,con=mc).save()
            return redirect('menu:pasta')
        elif mt=='risotto':
            Risotto(name=mn,price=mp,pic=mpic,con=mc).save()
            return redirect('menu:risotto')
        else:
            Drink(name=mn,price=mp,pic=mpic,con=mc).save()
            return redirect('menu:drink')
    return render(request, 'menu/create.html', context)


def delete(request,mpk):
    if Dish.objects.get(name=mpk):
        odi=Dish.objects.get(name=mpk)
        odi.pic.delete()
        odi.delete()
        return redirect('menu:dish')
    elif Pasta.objects.get(name=mpk):
        opa=Pasta.objects.get(name=mpk)
        opa.pic.delete()
        opa.delete()
        return redirect('menu:pasta')
    elif Risotto.objects.get(name=mpk):
        ori=Risotto.objects.get(name=mpk)
        ori.pic.delete()
        ori.delete()
        return redirect('menu:risotto')
    elif Drink.objects.get(name=mpk):
        odr=Drink.objects.get(name=mpk)
        odr.pic.delete()
        odr.delete()
        return redirect('menu:drink')
    return redirect('acc:index')
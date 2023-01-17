
from django.shortcuts import render
from .models import product
from .models import team

# Create your views here.
def home(request):
    obj=product.objects.all
    obj2 = team.objects.all
    return render(request,'index.html',{'product':obj,'team':obj2})



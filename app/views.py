from django.shortcuts import render

# Create your views here.

def condition(request):
    d={'name':'DAMARCHERLA CHANDU','age': 30 }
    return render(request, 'condition.html',context=d)

def forloop(request):
     d = ['Apple', 'Banana', 'Cherry', 'Date']
     return render(request, 'condition.html', {'items': d})

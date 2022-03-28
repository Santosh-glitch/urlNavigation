from django.shortcuts import render

# Create your views here.
def app2_specific(request):
    return render(request,'app2_specific.html')
from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def second_page(request):
    return render(request, 'second.html')
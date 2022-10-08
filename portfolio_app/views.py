from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'portfolio_base/index.html', {'t': [1, 2], 'm': [1, 2, 3], 'n': [1, 2, 3, 4]})

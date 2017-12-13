from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_page(request):
    return render(request, 'booking/home.html')

def categories_page(request):
    return render(request, 'booking/categories.html')


def pricing(request):
    return render(request, 'booking/pricing.html')


def maestro(request):
    return render(request,'booking/maestro.html')


def about_us(request):
    return render(request,'booking/about_us.html')

def contact(request):
    return render(request,'booking/contact.html')

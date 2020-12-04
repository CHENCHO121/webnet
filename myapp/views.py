from django.shortcuts import render
from .models import Contact

def home(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request,'index.html',context)


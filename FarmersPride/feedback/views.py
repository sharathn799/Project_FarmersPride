from django.shortcuts import render
from .models import Feedback

# Create your views here.
def feedback(request):
    if request.method == "POST":
           name = request.POST["name"]
           email = request.POST["email"]
           subject = request.POST["subject"]
           message = request.POST["message"]
           fd=Feedback(name=name,email=email,subject=subject,message=message)
           fd.save()
           return render(request, "feedback.html")
    else:
       return render(request, "contact.html")

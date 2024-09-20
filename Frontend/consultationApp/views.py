from django.shortcuts import render

def consultation_form(request):
    return render(request, 'consultationApp/consultation_form.html')

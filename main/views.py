from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406352424',
        'name': 'Haekal Alexander Dinova',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
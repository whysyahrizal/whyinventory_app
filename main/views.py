from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Wahyu Syahrizal',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
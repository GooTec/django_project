from django.shortcuts import  render


def index(request):
    return render(request, 'gui_project/index.html', {})


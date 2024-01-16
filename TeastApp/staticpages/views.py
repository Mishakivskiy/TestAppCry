from django.shortcuts import render


def api_documentation(request):
    return render(request, 'documentation.html')

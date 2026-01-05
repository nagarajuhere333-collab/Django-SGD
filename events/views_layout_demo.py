from django.shortcuts import render


def layout_options(request):
    """Demo view to show different layout options"""
    return render(request, 'events/layout_options.html')

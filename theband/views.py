from django.shortcuts import render, get_object_or_404
from .models import Band
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    Render the home page for the band application.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the home page template.
    """
    return render(request, 'band/homeband.html')

@login_required(login_url="user_auth:login")
def band_list(request):
    """
    Render a list of all bands.

    This view requires the user to be logged in. It fetches all Band
    objects from the database and renders them in the 'bandlist.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the band list template with the context
        containing the list of bands.
    """
    list_of_bands = Band.objects.all()
    context = {'list_of_bands': list_of_bands}
    return render(request, 'band/bandlist.html', context)

def band_detail(request, pk):
    """
    Render the details of a specific band.

    This view retrieves a Band object by its primary key (pk). If the band
    does not exist, a 404 error is raised. The details are rendered in the
    'bandDetail.html' template.

    Args:
        request: The HTTP request object.
        pk (int): The primary key of the band.

    Returns:
        HttpResponse: Renders the band detail template with the context
        containing the band information.
    """
    band = get_object_or_404(Band, pk=pk)
    context = {'band': band}
    return render(request, 'band/bandDetail.html', context)

from django.shortcuts import render
from lettings.models import Letting

# Create your views here.
# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci
# luctus et ultrices posuere cubilia curae; Cras eget scelerisque


def index(request):
    """
    Vue pour la page d'index des locations (lettings).

    Cette vue récupère la liste de toutes les locations (lettings) depuis la base de données
    et les transmet au template `lettings/index.html` via le contexte.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'lettings/index.html',
        incluant la liste des locations dans le contexte sous le nom 'lettings_list'.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, "lettings/index.html", context)

# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl
# id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut
# luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est
# luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris
# condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac
# lacinia augue pulvinar sit amet.


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique (letting).

    Cette vue récupère une location (letting) en fonction de l'identifiant donné
    et transmet ses informations au template `lettings/letting.html` via le contexte.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.
        letting_id (int): L'identifiant unique de la location à afficher.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'lettings/letting.html',
        incluant le titre et l'adresse de la location dans le contexte.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

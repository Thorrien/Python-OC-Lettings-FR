from django.shortcuts import render
from profiles.models import Profile

# Create your views here.

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat
# libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """
    Vue pour la page d'index des profils.

    Cette vue récupère la liste de tous les profils depuis la base de données
    et les transmet au template `profiles/index.html` via le contexte.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'profiles/index.html',
        incluant la liste des profils dans le contexte sous le nom 'profiles_list'.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et
# netus et males


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil utilisateur spécifique.

    Cette vue récupère un profil utilisateur en fonction du nom d'utilisateur donné
    et transmet ses informations au template `profiles/profile.html` via le contexte.

    Args:
        request (HttpRequest): L'objet de la requête HTTP.
        username (str): Le nom d'utilisateur de l'utilisateur dont on souhaite afficher le profil.

    Returns:
        HttpResponse: La réponse HTTP avec le rendu du template 'profiles/profile.html',
        incluant le profil de l'utilisateur dans le contexte sous le nom 'profile'.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

from django.contrib import admin
from django.urls import path

import lettings.views
import profiles.views


from oc_lettings_site import views


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings.views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
]

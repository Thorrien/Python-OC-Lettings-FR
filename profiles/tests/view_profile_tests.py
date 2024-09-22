import pytest
from django.urls import reverse
from profiles.models import User, Profile



@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, favorite_city='Paris')

@pytest.mark.django_db
def test_index_view_profile(client, profile):
    url = reverse('profiles_index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'profiles/index.html' in [t.name for t in response.templates]

    profiles_list = response.context['profiles_list']
    assert len(profiles_list) == 1
    assert profile in profiles_list

    content = response.content.decode()
    assert 'testuser' in content

@pytest.mark.django_db
def test_view_letting(client, profile):
    url = reverse('profile', args=[profile.user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert 'profiles/profile.html' in [t.name for t in response.templates]

    assert response.context['profile'] == profile

    content = response.content.decode()
    content = response.content.decode()
    assert profile.user.username in content
    assert profile.favorite_city in content
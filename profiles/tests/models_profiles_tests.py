import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from profiles.models import Profile


@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, favorite_city='Paris')


def test_profile_creation(profile):
    assert profile.pk is not None
    assert profile.user.username == 'testuser'
    assert profile.favorite_city == 'Paris'


def test_profile_str(profile):
    assert str(profile) == 'testuser'


def test_profile_user_relationship(profile):
    user = profile.user
    assert user.username == 'testuser'


def test_profile_deletion_on_user_delete(user, profile):
    user.delete()
    with pytest.raises(Profile.DoesNotExist):
        Profile.objects.get(pk=profile.pk)


def test_profile_favorite_city_blank(user):
    profile = Profile.objects.create(user=user)
    assert profile.favorite_city == ''


def test_profile_favorite_city_max_length(user):
    city = 'C' * 65
    profile = Profile(user=user, favorite_city=city)
    with pytest.raises(ValidationError) as excinfo:
        profile.full_clean()
    assert 'favorite_city' in excinfo.value.message_dict


def test_profile_unique_user(user):
    Profile.objects.create(user=user)
    profile2 = Profile(user=user)
    with pytest.raises(ValidationError) as excinfo:
        profile2.full_clean()
    assert 'user' in excinfo.value.message_dict

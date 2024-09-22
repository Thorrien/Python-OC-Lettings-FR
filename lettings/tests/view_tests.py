import pytest
from django.urls import reverse
from lettings.models import Letting, Address

@pytest.fixture
def address():
    return Address.objects.create(
        number=123,
        street='Main Street',
        city='Paris',
        state='FR',
        zip_code=75000,
        country_iso_code='FRA'
    )

@pytest.fixture
def letting(address):
    return Letting.objects.create(
        title='Charmante maison de ville',
        address=address
    )

@pytest.mark.django_db
def test_index_view_letting(client, letting):
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'lettings/index.html' in [t.name for t in response.templates]

    lettings_list = response.context['lettings_list']
    assert len(lettings_list) == 1
    assert letting in lettings_list

    content = response.content.decode()
    assert 'Charmante maison de ville' in content

@pytest.mark.django_db
def test_view_letting(client, letting):
    url = reverse('letting', args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert 'lettings/letting.html' in [t.name for t in response.templates]

    assert response.context['title'] == letting.title
    assert response.context['address'] == letting.address

    content = response.content.decode()
    content = response.content.decode()
    assert letting.title in content
    assert str(letting.address.number) in content
    assert letting.address.street in content
    assert letting.address.city in content
    assert letting.address.state in content
    assert str(letting.address.zip_code) in content
    assert letting.address.country_iso_code in content
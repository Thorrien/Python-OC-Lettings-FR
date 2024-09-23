import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting

@pytest.fixture
def valid_address_data():
    return {
        'number': 123,
        'street': 'Main Street',
        'city': 'Paris',
        'state': 'FR',
        'zip_code': 75000,
        'country_iso_code': 'FRA'
    }


@pytest.fixture
@pytest.mark.django_db
def address(valid_address_data):
    address = Address.objects.create(**valid_address_data)
    assert address.pk is not None
    assert str(address) == '123 Main Street'
    return address


@pytest.fixture
def valid_letting_data(address):
    return {
        'title': 'Charmante maison de ville',
        'address': address
    }


@pytest.fixture
def letting(valid_letting_data):
    return Letting.objects.create(**valid_letting_data)


@pytest.mark.django_db
def test_address_full_clean(valid_address_data):
    address = Address(**valid_address_data)
    address.full_clean()


@pytest.mark.parametrize('invalid_number', [159654, 10000])
@pytest.mark.django_db
def test_address_number_invalid_values(invalid_number, valid_address_data):
    valid_address_data['number'] = invalid_number
    address = Address(**valid_address_data)
    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()
    assert 'number' in excinfo.value.message_dict


@pytest.mark.parametrize('invalid_state', ['F', 'FRA', ''])
@pytest.mark.django_db
def test_address_state_invalid_values(invalid_state, valid_address_data):
    valid_address_data['state'] = invalid_state
    address = Address(**valid_address_data)
    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()
    assert 'state' in excinfo.value.message_dict


@pytest.mark.parametrize('invalid_country_code', ['FR', 'FRAN', ''])
@pytest.mark.django_db
def test_address_country_iso_code_invalid_values(invalid_country_code, valid_address_data):
    valid_address_data['country_iso_code'] = invalid_country_code
    address = Address(**valid_address_data)
    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()
    assert 'country_iso_code' in excinfo.value.message_dict


@pytest.mark.django_db
def test_address_missing_required_fields():
    address = Address()
    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()
    required_fields = ['number', 'street', 'city', 'state', 'zip_code', 'country_iso_code']
    for field in required_fields:
        assert field in excinfo.value.message_dict


@pytest.mark.django_db
def test_letting_creation(letting):
    assert letting.pk is not None
    assert letting.title == 'Charmante maison de ville'
    assert letting.address is not None


@pytest.mark.django_db
def test_letting_str(letting):
    assert str(letting) == 'Charmante maison de ville'


@pytest.mark.django_db
def test_letting_address_relationship(letting):
    address = letting.address
    assert address.city == 'Paris'


@pytest.mark.django_db
def test_letting_deletion_on_address_delete(address, letting):
    address.delete()
    with pytest.raises(Letting.DoesNotExist):
        Letting.objects.get(pk=letting.pk)


@pytest.mark.django_db
def test_letting_title_max_length(address):
    title = 'A' * 257
    letting = Letting(title=title, address=address)
    with pytest.raises(ValidationError) as excinfo:
        letting.full_clean()
    assert 'title' in excinfo.value.message_dict


@pytest.mark.django_db
def test_letting_unique_address(address):
    Letting.objects.create(title='Letting 1', address=address)
    letting2 = Letting(title='Letting 2', address=address)
    with pytest.raises(ValidationError) as excinfo:
        letting2.full_clean()
    assert 'address' in excinfo.value.message_dict

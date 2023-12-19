# ----- 3rd Party Libraries -----
import pytest
from django.test import TestCase

# Create your tests here.
from base.models import Contact

# ----- Dummy Data -----

class DummyData:
    @staticmethod
    def dummy():
        data = {
            "name":"Owen",
            "email":"Owen@gmail.com",
            "subject":"Trial",
            "message":"this is a message"
        }

        return data

# ----- Assertion -----
class Assertion:
    def assertion(contact):
        assert contact.name == "Owen"
        assert contact.email == "Owen@gmail.com"
        assert contact.subject == "Trial"
        assert contact.message == "this is a message"

# ----- Test Endpoints -----

# test url
@pytest.mark.django_db
class TestUrl:
    def test_home_page_status_code(get, client):
        response = client.get('/api/contact/')
        assert response.status_code == 200


# ----- Test CRUD Models -----

@pytest.mark.django_db
class TestContact():
    # test create contact
    def test_create_contact(get, client):
        data = DummyData.dummy()

        contact = Contact.objects.create(**data)
        
        response = client.get('/api/contact/')
        assert response.status_code == 200

        mock_assert = Assertion
        mock_assert.assertion(contact)


    # test get contact
    def test_get_contact(get, client):
        data = DummyData.dummy()
        
        response = client.get('/api/contact/')
        assert response.status_code == 200

        contact = Contact.objects.create(**data)

        contact = Contact.objects.get(**data)

        mock_assert = Assertion
        mock_assert.assertion(contact)
        
        
    
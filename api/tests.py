from django.test import TestCase
from rest_framework.test import APIClient
from selenium import webdriver

# Create your tests here.


class TestSelenium(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_view_page(self):
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/')
        assert 'OK' in response.page_source
        assert '405' in response.page_source
        assert 'Allow' in response.page_source


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_view(self):
        response = self.client.get('http://127.0.0.1:8000/api/')
        self.assertEquals(response.status_code, 405)

    def test_failure(self):
        response = self.client.get('http://127.0.0.1:8000/api/')
        self.assertNotEquals(response.status_code, 200)


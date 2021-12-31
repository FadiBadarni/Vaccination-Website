from django.test import TestCase
from django.urls import reverse
from django.test import Client


class TestPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        url = reverse('Web-Home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')
        self.assertContains(response, 'COVID-19 Vaccination Variety')

    def test_about_page(self):
        url = reverse('About-Page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/about.html')
        self.assertContains(response, 'The Corona Virus')

    def test_faq_page(self):
        url = reverse('FAQ-Page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/FAQ.html')
        self.assertContains(response, 'Frequently Asked Questions')

    def test_contact(self):
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact-Page', 0, 301)


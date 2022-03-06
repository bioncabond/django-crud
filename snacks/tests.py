from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snack

# Create your tests here.

class SnacksTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snack.objects.create(
            name = 'chips', description = "you cant just have 1", purchaser = self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'chips')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'chips')

    def test_snack_description(self):
        self.assertEqual(f'{self.snack.description}', 'you cant just have 1')
    
    def test_username(self):
        self.assertEqual(f'{self.user.username}', 'tester')

    def test_user_email(self):
        self.assertEqual(f'{self.user.email}', 'tester@email.com')

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_detail_page_status_code(self):
        url = reverse('snack_detail', args="1")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_update_page_status_code(self):
        url = reverse('snack_update', args="1")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
      
    def test_delete_page_status_code(self):
      url = reverse('snack_delete', args="1")
      response = self.client.get(url)
      print(response)
      self.assertEqual(response.status_code, 200)
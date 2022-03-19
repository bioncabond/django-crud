from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Stuff

class StuffTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_stuff = Stuff.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_stuff.save()

    def test_stuffs_model(self):
        stuff = Stuff.objects.get(id=1)
        actual_owner = str(stuff.owner)
        actual_name = str(stuff.name)
        actual_description = str(stuff.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
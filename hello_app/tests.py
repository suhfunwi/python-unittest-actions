from django.test import SimpleTestCase

# Create your tests here.

class TestHelloMessage(SimpleTestCase):

    def test_hello_message(self):

        page = self.client.get('')   # get the home page
        self.assertContains(page, 'Hello everyone!')


class TestTwoPlusTwo(SimpleTestCase):
    
    def test_two_plus_two(self):
        page = self.client.get('/two_plus_two')
        self.assertContains(page, 4)


from django.test import TestCase

# Create your tests here.

class StatusAPITestCase(TestCase):
    """
    This class contains tests for the status list API endpoint.
    Args:
        TestCase (_type_): _description_
    """
    def test_status_list(self):
        """
        Test the status list API endpoint.
        """
        response = self.client.get('/api/status/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        
        
    def test_status_create(self):
        """
        Test the status create API endpoint.
        """
        data = {
            'text': 'Test status',
            'image_link': 'http://example.com/image.jpg',
            'is_active': True,
            'is_private': False
        }
        
        response = self.client.post('/api/status/create/', data)
        print(response.status_code)
        print(response.json())
        # self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['text'], data['text'])
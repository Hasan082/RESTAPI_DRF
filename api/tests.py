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
        
        




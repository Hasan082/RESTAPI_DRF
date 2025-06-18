from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from status.models import Status


class StatusAPITestCase(APITestCase):
    """
    Test suite for the Status API endpoints.
    """

    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

        # Create a test status instance
        self.status = Status.objects.create(
            text='Initial test status',
            is_active=True,
            is_private=False,
            user=self.user
        )

    def test_status_list(self):
        """
        Test retrieving the list of status entries.
        """
        response = self.client.get('/api/status/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreaterEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['text'], self.status.text)

    def test_status_create(self):
        """
        Test creating a new status entry via the API.
        """
        data = {
            'text': 'New test status',
            'is_active': True,
            'is_private': False
        }

        response = self.client.post('/api/status/create/', data, format='json')

        print("Status Code:", response.status_code)
        print("Response Data:", response.json())

        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['text'], data['text'])

    def test_status_create_with_image(self):
        """
        Test creating a status with an image upload.
        """
        image = SimpleUploadedFile(
            "test.jpg",
            b"file_content",
            content_type="image/jpeg"
        )

        data = {
            'text': 'Status with image',
            'image_link': image,
            'is_active': True,
            'is_private': False
        }

        response = self.client.post('/api/status/create/', data)

        self.assertEqual(response.status_code, 201)
        self.assertIn('image_link', response.json())
        self.assertEqual(response.json()['text'], data['text'])

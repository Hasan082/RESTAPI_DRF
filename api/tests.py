from django.contrib.auth.models import User
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from status.models import Status
from io import BytesIO
from PIL import Image


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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
            'is_private': False,
            'user': self.user.id
        }

        response = self.client.post('/api/status/create/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['text'], data['text'])
        

    def test_status_create_with_image(self):
        """
        Test creating a status with an image upload.
        """
        # Create a small valid image in memory
        image = BytesIO()
        Image.new('RGB', (1, 1)).save(image, 'JPEG')
        image.seek(0)
        
        uploaded_file = SimpleUploadedFile(
            name='test.jpg',
            content=image.read(),
            content_type='image/jpeg'
        )

        data = {
            'text': 'Status with image',
            'image_link': uploaded_file,
            'is_active': True,
            'is_private': False,
            'user': self.user.id
        }

        response = self.client.post('/api/status/create/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.json())
        self.assertEqual(response.json()['text'], data['text'])
        
        
    def test_status_update(self):
        """
        Test updating an existing status entry via the API.
        """
        data = {
            'text': 'Updated test status',
            'is_active': False,
            'is_private': True
        }

        response = self.client.patch(f'/api/status/update/{self.status.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.status.refresh_from_db()
        self.assertEqual(self.status.text, data['text'])
        self.assertFalse(self.status.is_active)
        self.assertTrue(self.status.is_private)
        
        
    def test_status_delete(self):
        """Test deleting an existing status entry via the API.
        """
        response = self.client.delete(f'/api/status/delete/{self.status.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Status.objects.filter(id=self.status.id).exists())
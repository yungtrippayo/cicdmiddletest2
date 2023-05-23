from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from .models import models
from datetime import timedelta
from django.utils import timezone

class GalleryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.image = models.objects.create(title='Test image', file='image.jpg', created_at=timezone.now())

    def test_gallery_view(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertContains(response, 'Test image')

class ImageDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.image = models.objects.create(title='Test image', file='image.jpg')

    def test_image_detail_view(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
        self.assertContains(response, 'Test image')


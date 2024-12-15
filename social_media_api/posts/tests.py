
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like
from notifications.models import Notification

class LikeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_like_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(f'/posts/{self.post.pk}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Like.objects.filter(post=self.post, user=self.user).exists())

    def test_unlike_post(self):
        self.client.login(username='testuser', password='password')
        self.client.post(f'/posts/{self.post.pk}/like/')
        response = self.client.post(f'/posts/{self.post.pk}/unlike/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Like.objects.filter(post=self.post, user=self.user).exists())


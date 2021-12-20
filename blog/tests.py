# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='a post title',
            slug='a-post-title',
            body='example body content'
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'a post title')
        self.assertEqual(f'{self.post.slug}', 'a-post-title')
        self.assertEqual(f'{self.post.body}', 'example body content')

    def test_post_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'example body content')
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail(self):
        response = self.client.get('/a-post-title')
        no_response = self.client.get('/post/not-a-post-title/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'example body content')
        self.assertTemplateUsed(response, 'post_detail.html')

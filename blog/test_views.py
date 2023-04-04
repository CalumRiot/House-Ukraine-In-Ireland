from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import CommentForm, PostForm


class TestViews(TestCase):
    
    # This method is called before each test case to set up any necessary objects.
    # In this case, it creates a user and a post that will be used in the tests.
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', slug='test-post', author=self.user, content='Test content')
    
    # Checks if the home page (index) is being displayed correctly.
    # It sends a GET request to the index URL and checks if the response contains the expected HTML content.
    def test_post_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    # Checks if the post detail page is being displayed correctly.
    # It sends a GET request to the URL for the test post created in setUp() and checks if the response contains the expected HTML content.
    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    # Checks if the post like functionality is working correctly.
    # It sends a POST request to the URL for the post like view and checks if the response redirects to the post detail page.
    # It also checks if the post is correctly added to the user's liked posts.
    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('post_like', args=[self.post.slug]))
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())
    
    # Checks if the about page is being displayed correctly.
    # It sends a GET request to the about URL and checks if the response contains the expected HTML content.
    def test_post_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About')
    
    # Checks if the post user page is being displayed correctly.
    # It sends a GET request to the post user URL and checks if the response contains the expected HTML content.
    # It also checks if the form used to create a post is being displayed correctly.
    def test_post_user_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post_user'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Post')
        self.assertIsInstance(response.context['post_form'], PostForm)

from django.test import TestCase
from blog.forms import CommentForm, PostForm
from blog.models import Comment, Post

# Create a User and Post object to use as foreign keys for the Comment model, Create a CommentForm instance with valid data and assert that the form is valid. In test_form_invalid_data, we create a CommentForm instance with invalid data (an empty body field) and assert that the form is not valid.


class CommentFormTest(TestCase):
    def test_form_valid_data(self):
        user = User.objects.create(username='testuser')
        post = Post.objects.create(title='Test Post', author=user, content='Test Content')
        form = CommentForm(data={'body': 'Test Comment',})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())

# Create a User object to use as the author for the Post model, Create a PostForm instance with valid data and assert that the form is valid. In test_form_invalid_data, we create a PostForm instance with invalid data and assert that the form is not valid.


class PostFormTest(TestCase):
    def test_form_valid_data(self):
        user = User.objects.create(username='testuser')
        form = PostForm(data={'title': 'Test Post', 'content': 'Test Content', 'author': user})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = PostForm(data={'title': '', 'content': '',})
        self.assertFalse(form.is_valid())

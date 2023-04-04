from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class BlogModelsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', author=self.user, content='Test Content')
        self.comment = Comment.objects.create(post=self.post, name='Test User', email='test@test.com', body='Test Comment')

# Checks that the __str__() method of the Post model returns the expected string representation of a post's title.
    def test_post_str_method(self):
        self.assertEqual(str(self.post), 'Test Post')

# Checks that the number_of_likes() method of the Post model returns 0 likes for a newly created post, since it hasn't been liked by anyone yet.
    def test_post_number_of_likes_method(self):
        self.assertEqual(self.post.number_of_likes(), 0)

# Checks that the __str__() method of the Comment model returns the expected string representation of a comment's body and author name.
    def test_comment_str_method(self):
        self.assertEqual(str(self.comment), 'Comment Test Comment by Test User')

# Checks that the slug field of a newly created Post model is correctly generated by the slugify function, which should remove any special characters and replace spaces with hyphens.
    def test_post_slugify_method(self):
        self.assertEqual(self.post.slug, 'test-post')

# Checks that the ordering meta option of the Post model is working correctly by creating two posts with different titles and checking that they are returned in reverse alphabetical order.
    def test_post_ordering(self):
        post1 = Post.objects.create(title='Post 1', author=self.user, content='Content 1')
        post2 = Post.objects.create(title='Post 2', author=self.user, content='Content 2')
        posts = Post.objects.all()
        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], post1)

# checks that the ordering meta option of the Comment model is working correctly by creating two comments on the same post with different author names and checking that they are returned in the order they were created.
    def test_comment_ordering(self):
        comment1 = Comment.objects.create(post=self.post, name='User 1', email='user1@test.com', body='Comment 1')
        comment2 = Comment.objects.create(post=self.post, name='User 2', email='user2@test.com', body='Comment 2')
        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment1)
        self.assertEqual(comments[1], comment2)

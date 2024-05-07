from django.test import TestCase
from .models import Post

class TestViews(TestCase):
    def test_blog_list_GET(self):
        post = Post.objects.create(
            title='Blog Title',
            sub_title='Blog Sub Title',
            body='Blog Content'
        )
        self.assertEqual(post.title, 'Blog Title')
        self.assertEqual(post.sub_title, 'Blog Sub Title')
        self.assertEqual(post.body, 'Blog Content')
        self.assertEqual(post.slug, 'blog-title')
        self.assertIsNotNone(post.published_date)
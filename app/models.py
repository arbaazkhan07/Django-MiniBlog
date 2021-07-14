from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    @staticmethod
    def show_posts():
        return Post.objects.all()

    @staticmethod
    def get_post(id):
        return Post.objects.get(pk=id)


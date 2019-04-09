from django.db import models

from django.utils import timezone

from markdownx.models import MarkdownxField

from markdownx.utils import markdownify


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    CATEGORY_CHOICES = (
    ('プログラミング', "Programming"),
    ('料理', "Cooking"),
    ('ゲーム', "Game"),
    ('映画', "Movie"),
    ('その他', "others"),
    )

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default="プログラミング")

    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    photo = models.ImageField(upload_to='documents/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def text_to_markdown(self):
        return markdownify(self.text)

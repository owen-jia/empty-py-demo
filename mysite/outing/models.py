from django.db import models


class Article(models.Model):
    """文章表"""

    title = models.TextField(null=False, blank=False, primary_key=True, max_length=200, unique=True)
    content = models.TextField(max_length=1000, default='', verbose_name='内容')
    publish_date = models.DateField(verbose_name='发布时间')

    def __str__(self):
        return self.title + " --- " + self.content

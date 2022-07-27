from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    content = models.TextField('내용', blank=True, null=True)
    score = models.IntegerField('별점', blank=True, null=True)
    source = models.CharField('구분', max_length=10, blank=True, null=True)
    at = models.DateTimeField('작성일', blank=True, null=True)
    def __str__(self):
        return f'{self.username} : {self.content}'

    class Meta:
        managed = True
        db_table = 'review'
        ordering = ['-at']
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'



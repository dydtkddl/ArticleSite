from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=3000, null=True)
    writer = models.CharField(max_length=3000, null=True)
    summary = models.TextField(null=True)
    content = models.TextField(null=True)
    conclusion = models.TextField(null=True)
    created_date = models.DateField(auto_now_add = True)
    modified_date = models.DateField(auto_now = True)
    concepts = models.ManyToManyField('Concept', through='ArticleConcept')
class Concept(models.Model):
    name = models.CharField(max_length=1000, null = True)
    detail = models.TextField(null=True)
class ArticleConcept(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    
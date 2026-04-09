from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Prompt(models.Model):
    text = models.TextField()
    llm = models.CharField(max_length=50)
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class TaggingMeta(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name="tags")
    topics = ArrayField(models.CharField(max_length=50))
    sentiment_score = models.FloatField(validators=[MinValueValidator(-1.0), MaxValueValidator(1.0)])
    sentiment_label = models.CharField(choices=["negative", "neutral", "positive"])
    stage = models.CharField(choices=["awareness", "consideration", "conversion", "loyalty"])

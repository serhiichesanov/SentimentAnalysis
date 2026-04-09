from .models import Prompt, TaggingMeta
from rest_framework import serializers


class PromptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prompt
        fields = ["url", "text", "llm", "answer", 'timestamp']


class TaggingMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaggingMeta
        field = ["url", "prompt", "topics", "sentiment_score", "sentiment_label", "stage"]
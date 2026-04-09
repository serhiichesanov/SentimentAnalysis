from SentimentApp.serializers import PromptSerializer, TaggingMetaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Prompt


@api_view(['GET', 'POST'])
def prompt(request):
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)

        return Response(serializer, status=status.HTTP_200_OK)
    else:
        serializer = PromptSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def summary(request):
    pass


@api_view(['GET'])
def topics(request):
    pass


@api_view(['GET'])
def stages(request):
    pass


@api_view(['GET'])
def insights(request):
    pass





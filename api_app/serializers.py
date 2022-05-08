from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     auther = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     datetime = serializers.DateTimeField()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'auther', 'email', 'datetime']

    # def create(self, validated_data):
    #      return Article.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.auther = validated_data.get('auther', instance.auther)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.datetime = validated_data.get('datetime', instance.datetime)
    #     instance.save()
    #     return instance
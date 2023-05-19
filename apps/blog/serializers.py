from rest_framework import serializers
from mptt.templatetags.mptt_tags import cache_tree_children

from .models import Category, Post, Tag, BannedWord


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'children',
        )

    def get_children(self, obj):
        children = obj.get_children()
        serializer = self.__class__(children, many=True)
        return serializer.data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )


class PostSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'pub_date',
            'update_date',
            'delete_date',
            'author',
            # 'tags',
        )

    def validate(self, data):
        errors = {}

        banned_words = BannedWord.objects.all()

        for word in banned_words:
            if word.word in data['title']:
                if errors.get('title'):
                    errors['title'].update({word.word: word.reason})
                else:
                    errors['title'] = {word.word: word.reason}

            if word.word in data['content']:
                if errors.get('content'):
                    errors['content'].update({word.word: word.reason})
                else:
                    errors['content'] = {word.word: word.reason}

        if errors:
            raise serializers.ValidationError(errors)

        return data


class BannedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedWord
        fields = (
            'id',
            'word',
            'reason',
        )

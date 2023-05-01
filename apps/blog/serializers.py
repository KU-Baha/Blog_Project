from rest_framework import serializers

from .models import Post, Tag, BannedWord


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

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
            'tags',
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

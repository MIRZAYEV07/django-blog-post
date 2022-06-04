from rest_framework.fields import SerializerMethodField
from ..models import  Post
from rest_framework import serializers

code_choices = [
    ("uz","Uzbek"),
    ("en-us","English"),
    ("ru","Russian")
 ]


class LanguageSerializer(serializers.Serializer):

    choices = serializers.ChoiceField(choices = code_choices)

class PostSerializer(serializers.ModelSerializer):
    post_categories = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='post_api:post', lookup_field='slug')

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'post_categories',
            'categories',
            'image',
            'views_counter',
            'active',
            'slug'
        ]
        read_only_fields = ('slug', 'post_categories', 'user')
        extra_kwargs = {
            'categories': {'write_only': True},
            'active': {'write_only': True}
        }

    def get_post_categories(self, obj):
        categories = obj.categories.all()
        return [categpry.name for categpry in categories]

    def get_author(self, obj):
        return obj.user.username


class PostDetailSerializer(serializers.ModelSerializer):
    post_categories = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'post_categories',
            'categories',
            'image',
            'views_counter',
            'active',
            'slug',

        ]
        read_only_fields = ('slug', 'post_categories', 'user')
        extra_kwargs = {
            'categories': {'write_only': True},
            'active': {'write_only': True}
        }

    def get_post_categories(self, obj):
        categories = obj.categories.all()
        return [categpry.name for categpry in categories]

    def get_author(self, obj):
        return obj.user.username

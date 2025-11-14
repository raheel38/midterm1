from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created_date', 'published_date', 'image', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return ""

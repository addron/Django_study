from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):

    def Meta(self):
        model = BookInfo
        fields = '__all__'


import os
# 我们单独运行 .py 文件的时候,需要配置一下django的环境变量, 如果是使用
# manager.py来运行的项目, 这个配置在django的manager.py中已经配置过了:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
from rest_framework import serializers


class User(object):

    def __init__(self, username, age):
        self.username = username
        self.age = age


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    age = serializers.IntegerField()


if __name__ == '__main__':
    user = User('战三', 18)

    serializer = UserSerializer(user)

    print(serializer.data)

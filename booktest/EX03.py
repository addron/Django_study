import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

from booktest.oldserializers import BookInfoSerializer
import django
django.setup()


if __name__ == '__main__':

    # 反序列化
    dict= {
        'btitle':'python',
        'bpub_date':'2012-12-12'
    }
    serializer = BookInfoSerializer(data=dict)

    # 验证  三步
    print(serializer.is_valid())
    # 抛出异常，程序结束
    # print(serializer.is_valid(raise_exception=True))
    print(serializer.errors)
    # print(serializer.validate)
    print(serializer.validated_data)
    serializer.save()
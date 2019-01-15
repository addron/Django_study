import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

from booktest.oldserializers import HeroInfoSerializer, BookInfoSerializer
import django

django.setup()

from booktest.models import HeroInfo, BookInfo

if __name__ == '__main__':
    hero = HeroInfo.objects.get(id=1)
    book = BookInfo.objects.get(id=1)
    serializer = HeroInfoSerializer(hero)
    serializer1 = BookInfoSerializer(book)
    print(serializer.data)
    print(serializer1.data)

from rest_framework import serializers

class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = serializers.CharField(max_length=20, label="名称")
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, default=0, label='性别')
    hcomment = serializers.CharField(max_length=200, label="描述信息")

class BookInfoSerializer(serializers.Serializer):
    btitle = serializers.CharField(max_length=20, label="书名")
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label="阅读量",default=0,required=False)
    bcomment = serializers.IntegerField(default=0,label="描述信息",required=False)
    image = serializers.ImageField(label='图片',required=False)


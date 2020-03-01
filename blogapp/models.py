from django.db import models
from tinymce.models import HTMLField


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True)  # 字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。但是之后的save()是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例save()之后赋值然后再save()。
    updated = models.DateTimeField(
        auto_now=True)  # auto_now=Ture，字段保存时会自动保存当前时间，但要注意每次对其实例执行save()的时候都会将当前时间保存，也就是不能再手动给它存非当前时间的值。

    class Meta:
        # 这个属性是定义当前的模型是不是一个抽象类。所谓抽象类是不会对应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段。
        abstract = True


class Cate(BaseModel):
    name = models.CharField(max_length=20, verbose_name="分类")

    class Meta:
        # 定义表名
        db_table = "cate_table"
        # 定义在管理后台显示的名称
        verbose_name = '分类'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=20, verbose_name="标签名")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag_table"
        # 定义在管理后台显示的名称
        verbose_name = '标签'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name


class Blog(BaseModel):
    title = models.CharField(max_length=30, verbose_name="标题")
    author = models.CharField(max_length=30, default="大海", verbose_name="作者")
    cate = models.ForeignKey(Cate, on_delete=True, verbose_name="分类")
    content = HTMLField(verbose_name="博客内容")
    desc = models.CharField(max_length=120, verbose_name="简介", default="")
    cat = models.IntegerField(default=0, verbose_name="浏览量")
    tags = models.ManyToManyField(Tag, related_name="blogs", verbose_name="多对多标签")

    class Meta:
        db_table = "blog_table"
        # 定义在管理后台显示的名称
        verbose_name = '博客'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(BaseModel):
    ip = models.CharField(max_length=32, verbose_name="评论人IP")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="评论的博客")
    content = models.CharField(max_length=120, verbose_name="评论内容")

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "comment_table"
        # 定义在管理后台显示的名称
        verbose_name = '评论'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=500, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=500, unique=True)


class ItemComponent(models.Model):
    name = models.CharField(max_length=500, unique=True)
    tags = models.ManyToManyField(Tag, related_name='items_components')


class Item(models.Model):
    name = models.CharField(max_length=500, unique=True)
    categories = models.ManyToManyField(Category, related_name='items')
    tags = models.ManyToManyField(Tag, related_name='items')
    components = models.ManyToManyField(ItemComponent, related_name='items')


class ItemFilePdf(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='files_pdf')
    file = models.FileField(upload_to='item/pdf')


class ItemFileVideo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='files_video')
    file = models.FileField(upload_to='item/video')


class ItemFileAudio(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='files_audio')
    file = models.FileField(upload_to='item/audio')

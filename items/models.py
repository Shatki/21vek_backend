from django.db import models


class Photo(models.Model):
    """ Изображения товаров и категорий
        У одного товара может быть несколько изображений
    """
    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = 'изображения'
        db_table = 'photo'

    url = models.URLField(verbose_name="изображение", null=False, blank=False)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return u'%s' % self.url


# Create your models here.
class Category(models.Model):
    """ Категории товаров
    """
    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = 'категории'
        db_table = 'category'

    # Идентификатор категории
    id = models.IntegerField(verbose_name=u"идентификатор категории", primary_key=True, blank=False)
    # Наименование категории
    name = models.CharField(verbose_name=u"наименование категории", max_length=100)
    # Идентификатор родительской категории
    parent_id = models.ForeignKey('self', verbose_name=u'идентификатор родительской категории',
                                  on_delete=models.CASCADE, blank=False)
    # Уровень вложенности категории
    # depth_level = models.IntegerField(verbose_name=u"уровень вложенности категории", blank=True)
    # Фото категории
    photo_list = models.ManyToManyField(Photo, verbose_name="Фото категории")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Item(models.Model):
    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = 'товары'
        db_table = 'items'

    # Идентификатор товара
    id = models.IntegerField(verbose_name=u"идентификатор товара", primary_key=True, blank=False)
    # Наименование товара
    name = models.CharField(verbose_name=u"наименование товара", max_length=200)
    # Категория товара
    category = models.ForeignKey(Category, verbose_name=u'Категория товара', on_delete=models.CASCADE, blank=False)
    # Артикулы поставщиков(для запроса)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

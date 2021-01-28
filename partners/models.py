from django.db import models
# Create your models here.


class Partner(models.Model):
    class Meta:
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        db_table = 'partners'

    name = models.CharField(verbose_name=u'наименование партнера', max_length=100, null=False)
    api_key = models.CharField(verbose_name=u'ключ API', max_length=100)
    api_url = models.CharField(verbose_name=u'API url', max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name

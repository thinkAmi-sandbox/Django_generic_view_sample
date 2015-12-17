from django.db import models

class Cultivar(models.Model):
    name = models.CharField(verbose_name="品種名", max_length=255)

    def __str__(self):
        # <select>で選択肢として表示する値を設定
        return self.name

class Place(models.Model):
    name = models.CharField(verbose_name="場所名", max_length=255)

    def __str__(self):
        return self.name

class TimeRange(models.Model):
    name = models.CharField(verbose_name="時間帯名", max_length=10)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    purchase_date = models.DateField(verbose_name="購入日")
    cultivars = models.ManyToManyField(Cultivar, verbose_name="品種")
    place = models.ForeignKey(Place, verbose_name="購入場所")
    is_fan = models.BooleanField(verbose_name="リピート購入")
    time_range = models.ForeignKey(TimeRange, verbose_name="時間帯")
    impression = models.TextField(verbose_name="感想")
    remarks = models.CharField(verbose_name="備考", max_length=255)

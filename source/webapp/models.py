from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=150, null=False, blank=False, verbose_name='Название категории')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Описание')

    def __str__(self):
        return f'{self.category}'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, blank=False, verbose_name="Описание")
    category = models.ForeignKey(to='webapp.Category', verbose_name='Категория', blank=False, null=False,
                                 related_name='products', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False, verbose_name='Стоимость')
    image = models.TextField(max_length=3000, null=False, blank=False, verbose_name="URL картинки")

    def __str__(self):
        return f'{self.name} - {self.price} | {self.added_at}'
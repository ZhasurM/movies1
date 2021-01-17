from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    name = models.CharField(verbose_name='Название', max_length=255, db_index=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d',verbose_name='Изображение', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name='Н')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])





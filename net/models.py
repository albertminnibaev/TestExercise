from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Net(models.Model):

    title = models.CharField(max_length=250, unique=True, verbose_name='наименование звена сети')
    email = models.EmailField(unique=True, verbose_name='адрес электронной почты', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    treet = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house = models.PositiveIntegerField(verbose_name='номер дома', **NULLABLE)
    net = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='поставщик',
                            related_name='provider')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='задолженость перед поставщиком', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):

    title = models.CharField(max_length=250, verbose_name='наименование продукта')
    model = models.CharField(max_length=250, verbose_name='модель продукта')
    product_launch_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    net = models.ForeignKey(Net, on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'












from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Net(models.Model):

    TYPE = (
        ('Завод', 'Завод'),
        ('Индивидуальный предприниматель', 'Индивидуальный предприниматель'),
        ('Розничная сеть', 'Розничная сеть')
    )

    title = models.CharField(max_length=250, unique=True, verbose_name='наименование звена сети')
    email = models.EmailField(unique=True, verbose_name='адрес электронной почты')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    treet = models.CharField(max_length=100, verbose_name='улица')
    house = models.PositiveIntegerField(verbose_name='номер дома')
    net = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='поставщик',
                            related_name='provider')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='задолженость перед поставщиком',
                               **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время и дата создания')
    type = models.CharField(max_length=50, default='Завод', choices=TYPE, verbose_name='тип звена сети')
    level = models.PositiveIntegerField(default=0, **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'


class Product(models.Model):

    title = models.CharField(max_length=250, verbose_name='наименование продукта')
    model = models.CharField(max_length=250, verbose_name='модель продукта')
    product_launch_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    net = models.ForeignKey(Net, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return f'{self.title} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

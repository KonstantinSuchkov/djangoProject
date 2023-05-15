from django.db import models

# Create your models here.


class ListOfKindergarden(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='действующий', default=True)

    def __str__(self):
        return self.name


class ListOfAreas(models.Model):
    kindergarden = models.ForeignKey(ListOfKindergarden, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='действующий', default=True)


class Accommodation(models.Model):
    kindergarden = models.ForeignKey(ListOfKindergarden, on_delete=models.CASCADE)
    area = models.ForeignKey(ListOfAreas, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название', max_length=128, unique=True)
    image = models.ImageField(upload_to='accommodation_img', blank=True)
    short_desc = models.TextField(verbose_name='краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    availability = models.PositiveIntegerField(verbose_name='свободных мест')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    group_desc = models.TextField(verbose_name='описание группы', max_length=60, blank=True)
    is_active = models.BooleanField(verbose_name='действует', default=True)

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by('kindergarden', 'area', 'name')

    def __str__(self):
        return f'{self.name} ({self.area.name})'

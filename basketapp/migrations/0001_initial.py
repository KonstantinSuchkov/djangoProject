# Generated by Django 4.0.10 on 2023-05-08 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeks', models.PositiveIntegerField(default=0, verbose_name='кол-во недель')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='время')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.accommodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование сырья')),
                ('fe', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Железо')),
                ('si', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Кремний')),
                ('al', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Алюминий')),
                ('ca', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Кальций')),
                ('s', models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Сера')),
            ],
            options={
                'verbose_name': 'Концентрат',
                'verbose_name_plural': 'Концентраты',
            },
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-04 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KindOfSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид спорта',
                'verbose_name_plural': 'Виды спорта',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Лига',
                'verbose_name_plural': 'Лиги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PariMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50, verbose_name='Игра')),
                ('total', models.FloatField(blank=True, verbose_name='Тотал матча')),
                ('more', models.FloatField(blank=True, verbose_name='Больше')),
                ('less', models.FloatField(blank=True, verbose_name='Меньше')),
                ('kindofsport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='parser_app.KindOfSport', verbose_name='Вид спорта')),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='parser_app.League', verbose_name='Лига')),
            ],
            options={
                'verbose_name': 'Обявления',
                'verbose_name_plural': 'Объявления',
                'ordering': ['total'],
            },
        ),
    ]

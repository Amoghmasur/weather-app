# Generated by Django 4.2.5 on 2023-09-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=120)),
                ('country', models.TextField(blank=True, max_length=50)),
                ('temperature', models.IntegerField(blank=True, default=0)),
                ('feels_like', models.IntegerField(blank=True, default=0)),
                ('weather_description', models.CharField(blank=True, max_length=120)),
                ('humidity', models.IntegerField(blank=True, default=0)),
                ('pressure', models.IntegerField(blank=True, default=0)),
                ('wind', models.IntegerField(blank=True, default=0)),
                ('longitude', models.CharField(blank=True, max_length=20)),
                ('latitude', models.CharField(blank=True, max_length=20)),
                ('weather_icon', models.CharField(blank=True, max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Прогноз погоды',
                'verbose_name_plural': 'Прогнозы погоды',
                'ordering': ['-created_at'],
            },
        ),
    ]
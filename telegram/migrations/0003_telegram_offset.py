# Generated by Django 2.1.7 on 2019-07-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_telegram_id_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='telegram_offset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('offset', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price1', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]

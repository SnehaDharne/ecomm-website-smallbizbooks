# Generated by Django 2.2.14 on 2022-04-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220420_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('H', 'Horror'), ('R', 'Romance'), ('P', 'Politics'), ('M', 'Mystery'), ('F', 'Fiction')], max_length=2),
        ),
    ]
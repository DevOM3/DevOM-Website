# Generated by Django 3.1.1 on 2020-09-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200908_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='playstore',
            name='imageURL',
            field=models.CharField(default='', max_length=521),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playstore',
            name='link',
            field=models.CharField(max_length=521),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-11 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
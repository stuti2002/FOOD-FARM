# Generated by Django 3.2.6 on 2021-11-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Phone_Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='Table_Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='Total_Item',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 2.2 on 2019-04-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=111, max_digits=15),
            preserve_default=False,
        ),
    ]

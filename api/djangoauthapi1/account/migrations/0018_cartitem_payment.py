# Generated by Django 4.2.1 on 2023-08-01 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_cartitem_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.payment'),
        ),
    ]

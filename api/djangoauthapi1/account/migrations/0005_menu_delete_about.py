# Generated by Django 4.2.1 on 2023-07-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='media/')),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
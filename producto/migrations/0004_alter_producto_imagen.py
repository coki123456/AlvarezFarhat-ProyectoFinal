# Generated by Django 5.0.3 on 2024-03-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_alter_producto_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos/'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-10 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshopapp', '0006_auto_20210505_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='digital',
            new_name='on_stock',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
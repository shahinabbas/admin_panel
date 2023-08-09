# Generated by Django 4.2.4 on 2023-08-07 10:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0019_rename_order_no_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
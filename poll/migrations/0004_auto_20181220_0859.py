# Generated by Django 2.1.4 on 2018-12-20 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20181220_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='creted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]

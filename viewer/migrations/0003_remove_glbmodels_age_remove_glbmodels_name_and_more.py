# Generated by Django 4.0.3 on 2022-03-13 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewer', '0002_alter_glbmodels_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glbmodels',
            name='age',
        ),
        migrations.RemoveField(
            model_name='glbmodels',
            name='name',
        ),
        migrations.AddField(
            model_name='glbmodels',
            name='lower_model',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='glbmodels',
            name='upper_model',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='glbmodels',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_content_options_alter_module_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='module',
            name='title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
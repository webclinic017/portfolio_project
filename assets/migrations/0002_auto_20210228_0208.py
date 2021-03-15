# Generated by Django 3.1.6 on 2021-02-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='asset_sector',
            new_name='asset_category',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_industry',
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_exchange',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Asset Exchange'),
        ),
    ]
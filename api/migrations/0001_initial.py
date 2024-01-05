# Generated by Django 4.2 on 2024-01-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='files')),
                ('pattern', models.CharField(choices=[('latin', 'latin'), ('cyrillic', 'cyrillic')], max_length=20)),
            ],
        ),
    ]

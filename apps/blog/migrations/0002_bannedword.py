# Generated by Django 4.2 on 2023-05-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True, verbose_name='Word')),
                ('reason', models.CharField(blank=True, max_length=200, verbose_name='Reason')),
            ],
            options={
                'verbose_name': 'Banned word',
                'verbose_name_plural': 'Banned words',
            },
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
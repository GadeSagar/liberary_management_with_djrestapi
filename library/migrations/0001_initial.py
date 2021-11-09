# Generated by Django 3.2.8 on 2021-10-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 2.0.8 on 2018-08-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MEA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='resources')),
            ],
        ),
    ]
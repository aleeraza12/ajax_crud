# Generated by Django 3.0.5 on 2020-04-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_ajax', '0004_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='static/files/')),
            ],
        ),
    ]
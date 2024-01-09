# Generated by Django 4.2.6 on 2024-01-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sprinciple', models.CharField(max_length=100)),
                ('slocation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('reenteremail', models.EmailField(max_length=254)),
            ],
        ),
    ]
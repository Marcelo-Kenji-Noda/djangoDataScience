# Generated by Django 3.1.2 on 2020-10-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

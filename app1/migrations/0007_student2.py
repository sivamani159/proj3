# Generated by Django 3.2 on 2022-09-07 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_student1_sesstime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
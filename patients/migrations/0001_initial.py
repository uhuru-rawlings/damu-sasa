# Generated by Django 4.2.1 on 2023-05-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=255)),
                ('Lname', models.CharField(max_length=255)),
                ('IdNumber', models.CharField(max_length=255, null=True)),
                ('PatientsNo', models.IntegerField()),
                ('FromTown', models.CharField(max_length=255)),
                ('FromVillage', models.CharField(max_length=255)),
                ('lastVisit', models.DateTimeField(auto_now=True)),
                ('dateAdded', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Patients',
            },
        ),
    ]
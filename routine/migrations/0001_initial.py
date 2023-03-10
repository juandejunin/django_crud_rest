# Generated by Django 3.2 on 2023-02-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('DepartamentsId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartamentsName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeesId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeesName', models.CharField(max_length=200)),
                ('Departament', models.CharField(max_length=200)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=200)),
            ],
        ),
    ]

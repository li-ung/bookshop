# Generated by Django 4.1.3 on 2022-11-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentInfo",
            fields=[
                (
                    "stu_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("stu_name", models.CharField(max_length=20)),
                ("stu_psw", models.CharField(max_length=20)),
            ],
        ),
    ]

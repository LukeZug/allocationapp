# Generated by Django 4.1.3 on 2023-01-23 13:53

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("allocationapp", "0004_auto_20230111_1556"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="preference",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="skills",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("skill_1", "Maths"),
                    ("skill_2", "Data Science"),
                    ("skill_3", "Programming"),
                    ("skill_4", "Critical Thinking"),
                    ("skill_5", "Statistics"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="technologies",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("technologies_1", "Python"),
                    ("technologies_2", "Java"),
                    ("technologies_3", "C/C++"),
                    ("technologies_4", "Haskell"),
                    ("technologies_5", "R"),
                ],
                max_length=50,
            ),
        ),
    ]

# Generated by Django 3.1.6 on 2023-01-24 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0002_auto_20230124_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='assigned_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='allocationapp.team'),
        ),
    ]
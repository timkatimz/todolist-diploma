# Generated by Django 4.1.3 on 2022-11-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_alter_goalcategory_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]